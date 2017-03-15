# coding=utf-8
import urllib, urllib2, json

from bot import bot

CHAT_ID = '224473640'


def rfpl():
    values = {"ajaxAction": "getTourStats","tour": 2327,"season": 685,}

    values = urllib.urlencode(values)
    req = urllib2.Request('http://rfpl.org/ajax/match/', values)
    data = json.load(urllib2.urlopen(req))

    if u'Дата уточняется' != data['contents'][0]['date']:
        bot.sendMessage(chat_id=CHAT_ID, text='rfpl: calendar change!')

    return 'ok'
