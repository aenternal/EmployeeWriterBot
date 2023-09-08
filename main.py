import telebot
from telebot import types
from config import TOKEN
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from states import BotStates
from database.db import Session
from database.models import User
from values_generator import values_gen
from excel_module.excel_write import export


state_storage = StateMemoryStorage()

bot = telebot.TeleBot(TOKEN, state_storage=state_storage)


def main_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Записать работника', callback_data='write_employee'),
        types.InlineKeyboardButton('Завершить работу', callback_data='bye_bye')
    )
    bot.set_state(message.from_user.id, BotStates.await_callback)
    bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)


# Handle '/start'
@bot.message_handler(commands=['start'])
def start(message):
    main_menu(message)


@bot.callback_query_handler(state=BotStates.await_callback, func=lambda call: True)
def callback(call):
    if call.data == 'write_employee':  # Проверка, на какую кнопку нажал юзер
        bot.set_state(call.from_user.id, BotStates.employee_proceed)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Введите ФИО работника:')
    elif call.data == 'bye_bye':
        bot.set_state(call.from_user.id, BotStates.menu)
        bot.send_message(call.message.chat.id, 'Работа окончена! Чтобы вызвать меня снова, введите команду /start')


@bot.message_handler(state=BotStates.employee_proceed)
def employee_proceed(message):
    session = Session()
    values = values_gen(session)
    fio = message.text
    employee = User(
        fio=fio,
        id=values[0],
        datar=values[1],
        id_role=values[2],
    )
    session.add(employee)
    session.commit()
    export(session)
    session.close()
    bot.send_document(message.chat.id, document=open('employees.xlsx', 'rb'))
    bot.set_state(message.from_user.id, BotStates.menu)
    main_menu(message)


bot.add_custom_filter(custom_filters.StateFilter(bot))

bot.infinity_polling()
