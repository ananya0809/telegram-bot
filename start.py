import telebot
from config import Config
bot = telebot.TeleBot(Config.API_KEY, parse_mode=None)

class MsgHandler:
    @bot.message_handler(commands=['hi'])
    def hi(message):
        bot.send_message(message.chat.id, "Hello!")
    @bot.message_handler(func=lambda message: True) 
    def echo_all(message):
	    bot.reply_to(message, message.text)
bot.polling()