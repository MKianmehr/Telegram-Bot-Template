import os

import telebot

bot = telebot.TeleBot(
    os.environ['STRANGERS_BOT_TOKEN'], parse_mode='HTML'
) 
