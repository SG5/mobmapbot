import urllib2, binascii

from bot import bot

CHAT_ID = '224473640'


def tele2():
    try:
        urllib2.urlopen('http://msk.tele2.ru/CoverageData/regions/msk/_3g/12/2476/1292.png')
        try:
            urllib2.urlopen('http://msk.tele2.ru/CoverageData/regions/msk/_lte/12/2476/1292.png')
            bot.sendMessage(chat_id=CHAT_ID, text='tele2: LTE work!')
        except urllib2.HTTPError as e:
            if 404 == e.code:
                bot.sendMessage(chat_id=CHAT_ID, text='tele2: 3g exist, LTE not found')
    except urllib2.HTTPError as e:
        if 404 == e.code:
            bot.sendMessage(chat_id=CHAT_ID, text='tele2: 3g not found')

    return 'ok'


def beeline():
    response = urllib2.urlopen('http://h01tiles2.tmcrussia.com/bee4g-sem/lv17/00/000/079/224/000/089/233.png')
    if 970488898 == binascii.crc32(response.read()):
        bot.sendMessage(chat_id=CHAT_ID, text='beeline: 4g not found')
    else:
        bot.sendMessage(chat_id=CHAT_ID, text='beeline: LTE work!')

    return 'ok'
