from aiogram.fsm.state import StatesGroup, State


class SendMessage(StatesGroup):
    message = State()
    author = State()
