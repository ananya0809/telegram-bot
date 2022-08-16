import telebot

class BotHandler:
    def __init__(self, apikey):
        self.bot = telebot.TeleBot(apikey, parse_mode=None)
