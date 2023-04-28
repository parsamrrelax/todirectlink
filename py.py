import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import subprocess

# Define your Telegram bot token and Transmission credentials here
BOT_TOKEN = 'YOURBOTTOKEN'
TRANSMISSION_HOST = 'localhost'
TRANSMISSION_PORT = '9091'
TRANSMISSION_USERNAME = 'transmission'
TRANSMISSION_PASSWORD = 'transmission'


# Initialize the Telegram bot
bot = telegram.Bot(token=BOT_TOKEN)

# Define the /magnet command handler function
def magnet_handler(update, context):
    # Send a message to the user requesting their magnet link
    update.message.reply_text('Insert your magnet link')

# Define the message handler function
def message_handler(update, context):
    # Get the user's message text
    message_text = update.message.text.strip()

    # Check if the message text is a valid magnet link
    if message_text.startswith('magnet:'):
        # If it is, send a "correct link" message to the user
        update.message.reply_text('Correct link')
        # Use transmission-remote to add the magnet link to Transmission
        result = subprocess.check_output(['systemctl', 'restart', 'transmission-daemon.service'])
        os.system(f'transmission-remote {TRANSMISSION_HOST}:{TRANSMISSION_PORT} -n "{TRANSMISSION_USERNAME}:{TRANSMISSION_PASSWORD}" -a "{message_text}"')
    else:
        # If it's not, send a "wrong link" message to the user
        update.message.reply_text('Wrong link')

# Initialize the updater and add the handlers
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('magnet', magnet_handler))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

# Start the bot
updater.start_polling()





