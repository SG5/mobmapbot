# coding=utf-8
import binascii, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, json

from bot import bot

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
    response = urllib.request.urlopen('https://travel.state.gov/content/travel/en/legal/visa-law0/visa-bulletin.html')
    if binascii.crc32(response.read()) != 1137916259:
        bot.sendMessage(chat_id=CHAT_ID, text='state.gov: new VB!')
    return 'ok'

