import os
import telebot
apikey = os.getenv('API_KEY')
bot = telebot.TeleBot(apikey, parse_mode=None)

@bot.message_handler(commands=['hi'])
def hi(message):
    bot.send_message(message.chat.id, "Hello!")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
bot.polling()