from flask import Flask, render_template

import controller as controller

app = Flask(__name__)


@app.route('/growbot')
def index():
    humidity = controller.get_moisture_readings();
    return render_template('index.html', text="G R O W B O T", humidity=humidity)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
