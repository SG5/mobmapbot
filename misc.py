# coding=utf-8
import binascii, urllib, urllib2, json

from bot import bot

CHAT_ID = '224473640'


def rfpl():
    values = urllib.urlencode({"ajaxAction": "getTourStats","tour": 2328,"season": 685,})
    req = urllib2.Request('http://rfpl.org/ajax/match/', values)
    data = json.load(urllib2.urlopen(req))

    if u'Дата уточняется' != data['contents'][6]['date']:
        bot.sendMessage(chat_id=CHAT_ID, text='rfpl: calendar change!')

    return 'ok'


def velobike():
    response = urllib2.urlopen('http://velobike.ru/news/')
    if (-1774534778) != binascii.crc32(response.read()):
        bot.sendMessage(chat_id=CHAT_ID, text='velobike: news updated!')
    return 'ok'
