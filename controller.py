import pifaceio, time

# input 0 - 5 are connected to soil moisture sensors
moisture_sensor_list = [0, 1, 2, 3, 4, 5]
# output 2 is providing grounding to moisture sensors only when needed
enable_sensors = 2;
# output 0 and 1 are connected in parallel to the relays feeding the pumps
pump_list = [0, 1]

pf = pifaceio.PiFace()

# state holds the last readings from the moisture sensors
state = []

# get the readings from all connected moisture sensors
def get_moisture_readings():
    # enable sensors before reading values
    pf.write_pin(enable_sensors, 1)
    for sensor in moisture_sensor_list:
        state.append(pf.read_pin(sensor))
        print("reading sensor ", sensor)
        print("general state: ", pf.read())
    # disable sensors when done
    pf.write_pin(enable_sensors, 0)
    return state;


def pump_all():
    for pump in pump_list:
        pf.write_pin(pump, 1)
        print ("pumping " + pump)
        time.sleep(3)
        print ("stopping " + pump)
        pf.write(pump, 0)
    return
