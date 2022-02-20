from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def index():
    return """<!DOCTYPE HTML>
    <html>
        <head>
            <title>Второй пример</title>
        </head>
        <body bgcolor=blue text=white>
            <h1>Привет!</h1>
        </body>
    </html>"""


@app.route('/bye')
def bye():
    return """<!DOCTYPE HTML>
    <html>
        <head>
            <title>Второй пример</title>
        </head>
        <body bgcolor=blue text=white>
            <h1>Пока!</h1>
        </body>
    </html>"""

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

