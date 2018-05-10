import pifaceio, time, logcontroller, datetime

# input 0 - 5 are connected to soil moisture sensors
moisture_sensor_list = [0, 1, 2, 3, 4, 5]
# output 2 is providing grounding to moisture sensors only when needed
enable_sensors = 2;
# output 0 and 1 are connected in parallel to the relays feeding the pumps
pump_list = [0, 1]

pf = pifaceio.PiFace()

moisture = "moisture"
wet = "wet"
dry = "dry"
pumped = "pumped"


# get the readings from all connected moisture sensors
def get_moisture_readings():
    state = []
    # enable sensors before reading values
    pf.write_pin(enable_sensors, 1)
    pf.write()
    pf.read()
    for sensor in moisture_sensor_list:
        state.append(wet if pf.read_pin(sensor) else dry)
        print("reading sensor ", sensor)
        print("general state: ", pf.read())
    # disable sensors when done
    pf.write_pin(enable_sensors, 0)
    pf.write()
    logcontroller.append_row(moisture, state)
    return state


# run one specific pump
def pump(pump_id):
    pump_id_int = int(pump_id)
    if pump_id_int in pump_list:
        pf.write_pin(pump_id_int, 1)
        pf.write()
        print ("pumping " + pump_id)
        time.sleep(3)
        print ("stopping " + pump_id)
        pf.write_pin(pump_id_int, 0)
        pf.write()
        logcontroller.append_row(pumped,  pump_id_int)
        return 1
    else:
        print "No pump with id: " + pump_id
        return -1

# run the pumps in sequence
def pump_all():
    for pump in pump_list:
        pf.write_pin(pump, 1)
        pf.write()
        print ("pumping " + str(pump))
        time.sleep(3)
        print ("stopping " + str(pump))
        pf.write_pin(pump, 0)
        pf.write()
        logcontroller.append_row(pumped,  pump)
    return
