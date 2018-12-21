# coding=utf-8
import binascii
from datetime import datetime
import json
import re
import urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from init import bot, db

CHAT_ID = '224473640'


def rfpl():
    values = urllib.parse.urlencode({"ajaxAction": "getTourStats","tour": 2328,"season": 685,})
    req = urllib.request.Request('http://rfpl.org/ajax/match/', values)
    data = json.load(urllib.request.urlopen(req))

    if 'Дата уточняется' != data['contents'][6]['date']:
        bot.sendMessage(chat_id=CHAT_ID, text='rfpl: calendar change!')

    return 'ok'


def velobike():
    response = urllib.request.urlopen('http://velobike.ru/news/')
    if (-1774534778) != binascii.crc32(response.read()):
        bot.sendMessage(chat_id=CHAT_ID, text='velobike: news updated!')
    return 'ok'


def visa_bulletin():
    now = datetime.utcnow()
    next_bulletin = (now.replace(month=now.month+1) if now.month < 12 else now.replace(month=1, year=now.year+1)).strftime('%B %Y')

    if not db.bulletins.find_one({'name': next_bulletin}):
        url = 'https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin.html'
        response = urllib.request.urlopen(url)
        response_data = response.read().decode()

        search_result = re.search(f'<a.+?href="(.+?)".+?{next_bulletin}', response_data)

        if search_result:
            chats = [CHAT_ID, '-1001110150719']
            bulletin_url = 'https://travel.state.gov' + search_result.group(1)
            reply_links = [[
                InlineKeyboardButton(next_bulletin, url=bulletin_url)
            ]]

            for chat in chats:
                bot.sendMessage(
                    chat_id=chat, parse_mode='Markdown',
                    text=f'🇺🇸🤠🇺🇸\n*{next_bulletin}* VB has been released!',
                    reply_markup=InlineKeyboardMarkup(reply_links)
                )
            db.bulletins.insert_one({'name': next_bulletin})

            response = urllib.request.urlopen(bulletin_url)
            response_data = response.read().decode()

            search_result = re.search('EUROPE.+?EUROPE.+?([\d,]+)', response_data, re.DOTALL)

            if search_result:
                for chat in chats:
                    bot.sendMessage(
                        chat_id=chat, parse_mode='Markdown',
                        text=f'New case number: *{search_result.group(1)}*\n😱'
                    )

    return 'ok'

