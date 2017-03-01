import urllib2

from bot import bot

CHAT_ID = '224473640'


def Chekhov():
    process_tower_status(4884)
    return 'ok'


def Serpukhov():
    process_tower_status(4873)
    return 'ok'


def Butovo():
    process_tower_status(4894)
    return 'ok'


def process_tower_status(nodeid):
    text = ''
    statuses = get_tower_status(nodeid)

    for status in statuses:
        text += ', '.join(status) + '\r\n'

    bot.sendMessage(chat_id=CHAT_ID, text=text)


def get_tower_status(nodeid):
    url = 'http://xn--80aa2azak.xn--p1aadc.xn--p1ai/rtrs/ajax/node?node={}&multiplex=1'.format(nodeid)
    html = urllib2.urlopen(url).read()

    start = html.find('<h4') + 1

    tower_title_tag = html.find('<div', start + 1)
    tower_title = html[html.find('>', tower_title_tag) + 1: html.find('</div>', tower_title_tag)]
    result = [(tower_title,)]

    while True:
        title_tag = html.find('<h4', start)
        if -1 == title_tag:
            break

        title = html[html.find('>', title_tag) + 1: html.find('</h4>', title_tag)]

        frequency_tag = html.find('<div', title_tag + 1)
        frequency = html[html.find('>', frequency_tag) + 1: html.find('</div>', frequency_tag)]

        status_tag = html.find('<div', frequency_tag + 1)
        status = html[html.find('>', status_tag) + 1: html.find('</div>', status_tag)]

        start = status_tag + 1
        result.append((title, frequency, status,))

    return result
