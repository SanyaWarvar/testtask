from aiogram.client.session import aiohttp
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Router
from bot_config import BASE_API_URL
from states import SendMessage

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Hello world!")


@router.message(Command("get_messages"))
async def get_messages_handler(message: Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://{BASE_API_URL}/api/v1/messages") as response:
            data = await response.json()
    messages = "Все сообщения:\n" + "\n\n".join(
        [
            f"Текст: {item['text']}\nАвтор: {item['author']}" for item in data
        ]
    )

    if len(data) == 0:
        messages = "Сообщений нет!"

    await message.answer(messages)


@router.message(Command("send_message"))
async def send_message(message: Message, state: FSMContext):
    await state.set_state(SendMessage.message)
    await message.answer("Введите текст сообщения:")


@router.message(SendMessage.message)
async def send_message2(message: Message, state: FSMContext):
    await state.update_data(message=message.text, author=message.from_user.full_name)
    data = await state.get_data()

    async with aiohttp.ClientSession() as session:
        async with session.post(f"http://{BASE_API_URL}/api/v1/message", json=data) as response:
            if response.status == 201:
                await message.answer("Сообщение успешно сохранено!")
            else:
                await message.answer("Произошла ошибка!")
    await state.clear()
