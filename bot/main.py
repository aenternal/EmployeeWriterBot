import telebot
from telebot import types
from bot.core.config import TOKEN


bot = telebot.TeleBot(TOKEN)


def main_menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    write_button = types.InlineKeyboardButton('Записать работника', callback_data='write_employee')
    end_button = types.InlineKeyboardButton('Завершить работу', callback_data='bye_bye')
    markup.add(write_button, end_button)
    return bot.send_message(message.chat.id, 'Главное меню', reply_markup=markup)


def promt_for_input(message):
    msg = bot.send_message(message.chat.id, 'Введите ФИО работника')
    bot.register_message_handler(msg, response_proceed)


def response_proceed(message):
    user_response: str = message.text  # тут хранится наш ответ, дальше можно его обрабатывать
    fio = user_response.split(sep=' ')
    if len(fio) < 3:
        bot.send_message(message.chat.id, 'Ну нет, введите ответ в формате:\nФамилия Имя Отчество')
    else:
        bot.reply_to(message.chat.id, 'Работник успешно записан!')


def write_employee(fio):
    pass


# Handle '/start'
@bot.message_handler(commands=['start'])
def start(message):
    # async with engine.begin() as conn:
    #     await conn.runsync(models.Base.metadata.create_all())
    msg = main_menu(message)
    bot.register_next_step_handler(msg, callback)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    message = call.message
    if call.data == 'write_employee':  # Проверка, на какую кнопку нажал юзер
        msg = bot.send_message(message.chat.id, 'Начинаю работу...')
        promt_for_input(msg)
    elif call.data == 'bye_bye':
        bot.send_message(message.chat.id, 'Работа окончена! Чтобы вызвать меня снова, введите команду /start')


# # Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, 'Для вход')


bot.infinity_polling()
