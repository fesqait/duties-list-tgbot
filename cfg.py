from telegram.ext.updater import Updater
from telegram import Bot

TOKEN = "ur token here"
#   your token here
updater = Updater(TOKEN, use_context=True)

bot = Bot(token=TOKEN)

ADMIN = [
    664945442,
]