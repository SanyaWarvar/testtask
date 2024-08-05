import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from handlers import router as handle_router
from bot_config import BOT_TOKEN


def get_commands() -> list:
    bot_commands = [
        BotCommand(command="/get_messages", description="Получить все сообщения"),
        BotCommand(command="/send_message", description="Отправить новое сообщение")
    ]
    return bot_commands


async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    bot_commands = get_commands()
    await bot.set_my_commands(bot_commands)

    dp = Dispatcher()
    dp.include_router(handle_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
