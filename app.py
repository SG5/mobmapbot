import os

from flask import Flask

import misc

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/misc/vb', methods=['GET'])
def tele2Handler():
    return misc.visa_bulletin()


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))