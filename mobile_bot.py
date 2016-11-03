import urllib2, binascii

from google.appengine.api import app_identity
from hashlib import sha256
from flask import request
from secret import get_bot_token as token
import telegram

bot = telegram.Bot(token=token())
WEB_HOOK_URL = sha256(token()).hexdigest()


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


def tele2():
    try:
        urllib2.urlopen('http://msk.tele2.ru/CoverageData/regions/msk/_3g/12/2476/1292.png')
        try:
            urllib2.urlopen('http://msk.tele2.ru/CoverageData/regions/msk/_lte/12/2476/1292.png')
            bot.sendMessage(chat_id='224473640', text='tele2: LTE work!')
        except urllib2.HTTPError as e:
            if 404 == e.code:
                bot.sendMessage(chat_id='224473640', text='tele2: 3g exist, LTE not found')
    except urllib2.HTTPError as e:
        if 404 == e.code:
            bot.sendMessage(chat_id='224473640', text='tele2: 3g not found')

    return 'ok'


def beeline():
    response = urllib2.urlopen('http://h01tiles2.tmcrussia.com/bee4g-sem/lv17/00/000/079/224/000/089/233.png')
    if 970488898 == binascii.crc32(response.read()):
        bot.sendMessage(chat_id='224473640', text='beeline: 4g not found')
    else:
        bot.sendMessage(chat_id='224473640', text='beeline: LTE work!')

    return 'ok'


def get_webhook_url():
    return WEB_HOOK_URL


def send_webhook_url():
    bot.setWebhook(app_identity.get_default_version_hostname() + "/" + WEB_HOOK_URL)
