import telebot
from telebot import types
from telebot.types import WebAppInfo
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()
secret_bot_key = str(os.getenv('SECRET_BOT_KEY_DATA'))
bot = telebot.TeleBot(secret_bot_key)


@bot.message_handler(commands=['start'])
def start_command_func(message):
    bot.send_message(message.chat.id, "Hello, welcome to <b>Maxim's bot</b> application", parse_mode='html')


@bot.message_handler(commands=['time'])
def time_command_func(message):
    time_msg = str(datetime.now())
    answer_msg = "Current time: " + time_msg
    bot.send_message(message.chat.id, answer_msg)


@bot.message_handler(commands=['menu'])
def menu_command_func(message):
    website_url_string = "https://komax.space/"
    web_app_url_string = "https://komax.space/pageMiniApp.html"
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Open website", url=website_url_string))
    markup.add(types.InlineKeyboardButton("Mini app", web_app=WebAppInfo(url=web_app_url_string)))
    markup.add(types.InlineKeyboardButton("Show PI", callback_data="showPI"))
    markup.add(types.InlineKeyboardButton("Show E", callback_data="showE"))
    markup.add(types.InlineKeyboardButton("Hello", callback_data="helloMsg"))
    bot.send_message(message.chat.id, "Choose action", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message_func(callback):
    if callback.data == "showPI":
        bot.send_message(callback.message.chat.id, "PI: 3,141592")
    elif callback.data == "showE":
        bot.send_message(callback.message.chat.id, "E: 2,7182")
    else:
        bot.send_message(callback.message.chat.id, "Hello, wonderful user!")


@bot.message_handler(commands=['meShort'])
def me_short_command_func(message):
    first_name = str(message.from_user.first_name)
    last_name = str(message.from_user.last_name)
    user_name = str(message.from_user.username)
    answer_text = first_name + "\n" + last_name + "\n" + user_name
    bot.send_message(message.chat.id, answer_text)


@bot.message_handler(commands=['me'])
def me_command_func(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler()
def simple_text_func(message):
    user_input_text = str(message.text)
    answer_text = "Your input text: " + user_input_text
    bot.send_message(message.chat.id, answer_text)


bot.polling(none_stop=True)

