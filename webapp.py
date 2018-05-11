from flask import Flask, render_template, request, jsonify, Response

import iocontroller
import weathercontroller
import logcontroller
app = Flask(__name__)


@app.route('/growbot', methods=['GET', 'POST'])
def index():
    humidity = iocontroller.get_moisture_readings()
    if request.method == 'POST':
        iocontroller.pump_all()

    temperature = weathercontroller.get_current_temp()
    return render_template('index.html', text="G R O W B O T", humidity=humidity, temp=temperature[1],
                       city=temperature[0], temptime=temperature[2])


@app.route('/growbot/api/event_logs', methods=['GET'])
def get_logs():
    start = request.args.get('start', 0, type=int)
    end = request.args.get('end', 0, type=int)
    event_type = request.args.get("type", None)
    limit = request.args.get("limit", 1000, type=int)
    if start != 0 or end != 0 :
        all_rows = logcontroller.get_rows_between(start, end, event_type, limit)
    else:
        all_rows = logcontroller.get_all_rows(event_type, limit);
    return jsonify('event_logs', all_rows)


@app.route('/growbot/api/pump/', defaults={'pump_id': None}, methods=['POST'])
@app.route('/growbot/api/pump/<pump_id>', methods=['POST'])
def pump(pump_id):
    result = 1
    if pump_id is None:
        iocontroller.pump_all()
    else:
        result = iocontroller.pump(pump_id)
    return Response() if result == 1 else Response("No such pump", 400)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
