import os

from flask import Flask

import bot
import mobile
import tv

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/' + bot.get_webhook_url(), methods=['POST'])
def webhook_handler():
    return bot.webhook_handler()


@app.route('/3g/tele2', methods=['GET'])
def tele2Handler():
    return mobile.tele2()


@app.route('/4g/beeline', methods=['GET'])
def beelineHandler():
    return mobile.beeline()


@app.route('/dvbt2/Chekhov', methods=['GET'])
def ChekhovHandler():
    return tv.Chekhov()


@app.route('/dvbt2/Serpukhov', methods=['GET'])
def SerpukhovHandler():
    return tv.Serpukhov()


@app.route('/dvbt2/Butovo', methods=['GET'])
def ButovoHandler():
    return tv.Butovo()


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))