import os

from flask import Flask

app = Flask('test app')

@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    debug = os.getenv('FLASK_DEBUG') == '1'
    app.run(debug=debug)
