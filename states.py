from telebot.handler_backends import StatesGroup, State


class BotStates(StatesGroup):
    menu = State()
    await_callback = State()
    input_employee = State()
    db_write_employee = State()
    send_employee_xlxs = State()
