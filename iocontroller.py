import pifaceio, time

# input 0 - 5 are connected to soil moisture sensors
moisture_sensor_list = [0, 1, 2, 3, 4, 5]
# output 2 is providing grounding to moisture sensors only when needed
enable_sensors = 2;
# output 0 and 1 are connected in parallel to the relays feeding the pumps
pump_list = [0, 1]

pf = pifaceio.PiFace()

# get the readings from all connected moisture sensors
def get_moisture_readings():
    state = []
    # enable sensors before reading values
    pf.write_pin(enable_sensors, 1)
    pf.write()
    pf.read()
    for sensor in moisture_sensor_list:
        state.append(pf.read_pin(sensor))
        print("reading sensor ", sensor)
        print("general state: ", pf.read())
    # disable sensors when done
    pf.write_pin(enable_sensors, 0)
    pf.write()
    return state;

# run the pumps in sequence
def pump_all():
    for pump in pump_list:
        pf.write_pin(pump, 1)
        pf.write()
        print ("pumping ")
        time.sleep(3)
        print ("stopping ")
        pf.write_pin(pump, 0)
        pf.write()
    return
