#Import libraries
from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
from like_db import LikeDB

#Import TOKEN from envoirment variable
TOKEN = '5549407151:AAGVaQx5L2bvwBYnZE3a50yycdBQfPvl1fo'

updater = Updater(TOKEN)
#Create start command handler
def start(update:Update, context:CallbackContext):
    """Starts with picture all likes and all dislikes"""
    
#Create updater and dispatcher
updater = Updater(TOKEN)

#add handler to updater
updater.dispatcher.add_handler(CommandHandler('start', start))

#Start the bot
updater.start_polling()
updater.idle()



