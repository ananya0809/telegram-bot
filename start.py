from config import Config
from bot_handler import BotHandler

bothandle = BotHandler(Config.API_KEY)
bothandle.setup_bot()
bothandle.set_and_get()
bothandle.start_polling()