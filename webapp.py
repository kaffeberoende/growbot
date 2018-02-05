from flask import Flask, render_template

app = Flask(__name__)


@app.route('/growbot')
def index():
    return render_template('index.html', text="G R O W B O T")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')