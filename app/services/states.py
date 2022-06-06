from aiogram.dispatcher.filters.state import State, StatesGroup


class LoadTest(StatesGroup):
    message = State()