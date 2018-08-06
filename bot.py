import os
from hashlib import sha256
from flask import request
import telegram

bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
WEB_HOOK_URL = sha256(os.environ['TELEGRAM_BOT_TOKEN']).hexdigest()


def webhook_handler():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True))

    if not update.message:
        return 'ok'

    chat_id = update.message.chat.id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    if update.message.text:
        bot.sendMessage(chat_id=chat_id, text=chat_id)

    return 'ok'


def get_webhook_url():
    return WEB_HOOK_URL


def send_webhook_url():
    bot.setWebhook(app_identity.get_default_version_hostname() + "/" + WEB_HOOK_URL)
