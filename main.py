from flask import Flask
import mobile_bot as bot

app = Flask(__name__)
bot.send_webhook_url()


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/' + bot.get_webhook_url(), methods=['POST'])
def webhook_handler():
    return bot.webhook_handler()


@app.route('/3g/tele2', methods=['GET'])
def tele2Handler():
    return bot.tele2()


@app.route('/4g/beeline', methods=['GET'])
def beelineHandler():
    return bot.beeline()


@app.route('/dvbt2/Chekhov', methods=['GET'])
def ChekhovHandler():
    return bot.Chekhov()


@app.route('/dvbt2/Serpukhov', methods=['GET'])
def SerpukhovHandler():
    return bot.Serpukhov()


@app.route('/dvbt2/Butovo', methods=['GET'])
def ButovoHandler():
    return bot.Butovo()


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
