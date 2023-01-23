#Import libraries
from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os
# from like_db import LikeDB
TOKEN = os.environ["TOKEN"]

#Import TOKEN from envoirment variable


updater = Updater(TOKEN)
#Create start command handler
def start(update:Update, context:CallbackContext):
    """Starts with picture all likes and all dislikes"""
    chat_id = update.message.chat.id

    bot = context.bot
    bot.sendMessage(
        chat_id="@ssstarts",
        text = "Xush kelibsiz",
    )
def sendImage(update:Update, contex:CallbackContext):

    bot = contex.bot
    image_id = update.message.photo.file_id

    
    
    


    
#Create updater and dispatcher
updater = Updater(TOKEN)

#add handler to updater
updater.dispatcher.add_handler(CommandHandler('start', start))



#Start the bot
updater.start_polling()
updater.idle()



