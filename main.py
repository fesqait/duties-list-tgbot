import telegram
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup
from telegram import User
from functools import wraps
from telegram.chat import ChatAction

#   some variables moved into that file cuz: 1 I dont know how to do rhis without them, 2 - less trash in main file :)
# import user_status as ust

#   Constants
#from cfg import updater
#from cfg import ADMIN
#from cfg import bot

#   Work with data
# import data as dt

#   print(update.message.chat_id) - gets user id
#   print('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))

global user


def delete_keyboard(update: Update):
    reply_markup = telegram.ReplyKeyboardRemove()
    bot.send_message(chat_id=update['message']['chat']['id'], 
        text=' ', 
        reply_markup=reply_markup
        )

def main():


    def start(update: Update, context: CallbackContext):
        global user

        user = update.message.from_user
        ust.user_id = user['id']
        update.message.reply_text(
            f"здравуствуйте {user['username']}, этот бот позволит получить от нашего курса ещё больше удовольствия! \nПожалуйста напишите /help чтобы увидеть все доступные команды")

    updater.dispatcher.add_handler(CommandHandler('start', start))

    @send_action(ChatAction.TYPING)
    def help(update: Update, context: CallbackContext):
        update.message.reply_text("""Доступные команды:
        /credits - Наши соцсети
        /reg - Регистрация, чтобы удостовериться что Вы член курса
        /gmail - To get gmail URL
        /geeks - To get the GeeksforGeeks URL""")
        if ust.isRegistered:
            update.message.reply_text("""Команды, доступные как участнику курса:
            /credits - Наши соцсети
            /reg - Регистрация, чтобы удостовериться что Вы член курса
            /gmail - To get gmail URL
            /geeks - To get the GeeksforGeeks URL""")
        print('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))

    updater.dispatcher.add_handler(CommandHandler('help', help))


    def get_credits(update: Update, context: CallbackContext):
        update.message.reply_text(
            "СЮДА НАПИСАТЬ ВСЕ СОЦСЕТИ"
            )

    updater.dispatcher.add_handler(CommandHandler('credits', get_credits))

    @send_action(telegram.constants.CHATACTION_TYPING)
    def registration(update: Update, context: CallbackContext):

        ust.isRegistrating = True
        #print(type(telegram.Chat.id))
        print(update['message']['chat']['id'])
        update.message.reply_text("Пожалуйста, напишите Ваш номер и фамилию. Эти данные нужны только чтобы узнать являетесь ли Вы участником. \nДанную процедуру надо проделать только один раз")

    updater.dispatcher.add_handler(CommandHandler('reg', registration))


    def linkedIn_url(update: Update, context: CallbackContext):
        update.message.reply_text(
            "LinkedIn URL => \
            https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/")


    def geeks_url(update: Update, context: CallbackContext):
        update.message.reply_text(
            "GeeksforGeeks URL => https://www.geeksforgeeks.org/")


    def unknown(update: Update, context: CallbackContext):
        update.message.reply_text(
            "Sorry '%s' is not a valid command" % update.message.text)

    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    @send_action(ChatAction.TYPING)
    def no_command_text(update: Update, context: CallbackContext):
        if ust.isRegistrating:
            # first - number(int), second - first surename(str)
            if update.message.text == 'Да':
                delete_keyboard(update)
                ust.isRegistrating = False
            elif update.message.text == 'Нет':
                delete_keyboard(update)
            else:

                reg_data = list(map(str, update.message.text.split()))
                custom_keyboard = [['Да'], ['Нет']]
                reply_markup = ReplyKeyboardMarkup(custom_keyboard)
                bot.send_message(chat_id=update['message']['chat']['id'], 
                        text="Вы ввели %s, всё верно?" % str(reg_data).replace("'", '')[1:-1],
                        reply_markup=reply_markup)

            
        else:
            update.message.reply_text(
                "Sorry I can't recognize you , you said '%s'" % update.message.text)

    updater.dispatcher.add_handler(MessageHandler(Filters.text and (~Filters.command), no_command_text))


    updater.start_polling()
    #updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
    #updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))



if __name__ == '__main__':
    main()