from telebot.handler_backends import StatesGroup, State


class BotStates(StatesGroup):
    menu = State()
    await_callback = State()
    employee_proceed = State()
