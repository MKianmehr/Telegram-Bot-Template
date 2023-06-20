import os

import telebot
from loguru import logger

from src.constants import keyboards


class Bot:
    """
    Telegram bot template
    """
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['STRANGERS_BOT_TOKEN'], parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
        self.echo_all = self.bot.message_handler(func=lambda message: True)(self.echo_all)

    def run(self):
        logger.info('Bot is running...')
        self.bot.infinity_polling()
    
    def echo_all(self, message):
        self.bot.send_message(
            message.chat.id, 
            message.text, 
            reply_markup=keyboards.main
        )


if __name__ == '__main__':
    logger.info('Bot started')
    bot = Bot()
    bot.run()