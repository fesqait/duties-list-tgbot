from telegram.ext.updater import Updater
from telegram import Bot

TOKEN = "2122593170:AAGMPWtzOFh7EqDmtaDfRIaBHcOGQ4bMukw"
#   your token here
updater = Updater(TOKEN, use_context=True)

bot = Bot(token=TOKEN)

ADMIN = [
    664945442,
]