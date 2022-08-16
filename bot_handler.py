import telebot

class BotHandler:
    def __init__(self, apikey):
        self.bot = telebot.TeleBot(apikey, parse_mode=None)
    
    def setup_bot(self):
        @self.bot.message_handler(commands=['hi'])
        def hi(message):
            self.bot.send_message(message.chat.id, "Hello!")
    
    def set_and_get(self):
        @self.bot.message_handler(commands=['set'])
        def set(message):
            try:
                self.num = int(message.text[4:])
                self.bot.reply_to(message, "OK" )
            except ValueError:
                self.bot.reply_to(message, "Please enter a number")

        @self.bot.message_handler(commands=['get'])
        def get(message):
            self.bot.reply_to(message, self.num)
    
    def start_polling(self):
        self.bot.polling()

