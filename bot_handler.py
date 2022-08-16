import telebot

class BotHandler:
    def __init__(self, apikey):
        self.bot = telebot.TeleBot(apikey, parse_mode=None)
    
    def setup_bot(self):
        @self.bot.message_handler(commands=['hi'])
        def hi(message):
            self.bot.send_message(message.chat.id, "Hello!")
        @self.bot.message_handler(func=lambda message: True) 
        def echo_all(message):
            self.bot.reply_to(message, message.text)
    
    def start_polling(self):
        self.bot.polling()

