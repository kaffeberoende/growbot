from flask import Flask, render_template, request

import iocontroller
import weathercontroller
app = Flask(__name__)


@app.route('/growbot', methods=['GET', 'POST'])
def index():
    humidity = iocontroller.get_moisture_readings()
    if request.method == 'POST':
        iocontroller.pump_all()

    temperature = weathercontroller.get_current_temp()
    return render_template('index.html', text="G R O W B O T", humidity=humidity, temp=temperature[1],
                       city=temperature[0], temptime=temperature[2])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
