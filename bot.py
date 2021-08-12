import logging

from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Dispatcher, Updater

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "1942673805:AAHhLRPk8kPjjBBFhj5xWMiWtJ3vRHxEPL0"


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello !"


@app.route(f'/{TOKEN}', methods=['GET', 'POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    dp.process_update(update)
    return "Ok"


def start(bot, update):
    print(update)
    author = update.message.from_user.first_name
    reply = "Hi {}". format(author)
    bot.send_message(chat_id=update.message.chat_id, text=reply)


def _help(bot, update):
    help_text = "hey! this is help text"
    bot.send_message(chat_id=update.message.chat_id, text=help_text)


def echo_text(bot, update):
    reply = update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=reply)


def echo_sticker(bot, update):
    bot.send_sticker(chat_id=update.message.chat_id,
                     sticker=update.message.sticker.file_id)


def error(bot, update):
    logger.error("Update '%s' caused error '%s'", update, update.error)


def main():
    bot = Bot(TOKEN)
    bot.set_webhook(" https://0e11fa2e7753.ngrok.io " + TOKEN)
    dp = Dispatcher(bot, None)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(MessageHandler("Filters.text", echo_text))
    dp.add_handler(CommandHandler("Filters.sticker", echo_sticker))
    dp.add_error_handler(error)


if __name__ == "__main__":
    main()
    Updater.idle()

app.run(port=80)