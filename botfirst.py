from asyncore import dispatcher

from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher, CallbackContext
from flask import Flask,request

TOKEN = "1942673805:AAHhLRPk8kPjjBBFhj5xWMiWtJ3vRHxEPL0"

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello !"


@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    update = Update.de_json(request.get_json(),Update)
    dispatcher.process_update(update)
    return "Ok"


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        f'Start the Script {update.effective_user.first_name}')


def _help(update: Update, context: CallbackContext) -> None:
    
    update.message.reply_text(
        f'How Can i Help you! {update.effective_user.first_name}')
    update.message.reply_text(
        f'is this a good time to talk to you {update.effective_user.first_name}')


updater = Updater('1942673805:AAHhLRPk8kPjjBBFhj5xWMiWtJ3vRHxEPL0')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("help", _help))


updater.start_polling()
updater.idle()
