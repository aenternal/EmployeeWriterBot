import telebot
import random
from telebot import types
from config import TOKEN
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from states import BotStates
from database.db import Session
from database.models import User, Role
from random_date import birthdate


state_storage = StateMemoryStorage()

bot = telebot.TeleBot(TOKEN, state_storage=state_storage)


def inline_keyboard_gen():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton('Записать работника', callback_data='write_employee'),
        types.InlineKeyboardButton('Завершить работу', callback_data='bye_bye')
    )
    return markup


# Handle '/start'
@bot.message_handler(commands=['start'])
def start(message):
    bot.set_state(message.from_user.id, BotStates.await_callback)
    markup = inline_keyboard_gen()
    bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)


@bot.message_handler(state=BotStates.input_employee)
def employee_proceed(message):
    write_session = Session()
    rand_date = birthdate()
    rand_role = random.randrange(1, write_session.query(Role).count())
    # Костыль, так как sqlite не позволяет использовать BIGINT в качестве первичного ключа с автоинкрементом
    rand_id = random.randint(10000, 1234567890)
    fio = message.text
    employee = User(
        fio=fio,
        datar=rand_date,
        id_role=rand_role,
        id=rand_id
    )

    write_session.add(employee)
    write_session.commit()
    # сomm1 = User(fio=message.text, datar=birthdate(), id_role=


@bot.callback_query_handler(state=BotStates.await_callback, func=lambda call: True)
def callback(call):
    if call.data == 'write_employee':  # Проверка, на какую кнопку нажал юзер
        bot.set_state(call.from_user.id, BotStates.input_employee)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Введите ФИО работника:')
    elif call.data == 'bye_bye':
        bot.send_message(call.message.chat.id, 'Работа окончена! Чтобы вызвать меня снова, введите команду /start')


bot.add_custom_filter(custom_filters.StateFilter(bot))

bot.infinity_polling()
