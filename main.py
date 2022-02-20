from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def index():
    return render_template('base.html', emotion="Привет", name="Yandex")


@app.route('/bye')
def bye():
    return render_template('base.html', emotion="Пока", name="Yandex")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
