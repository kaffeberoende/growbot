import pifaceio, time

hum_sense_list = [0, 1, 2, 3]
pump_list = [15, 16]
pf = pifaceio.PiFace()

def get_humidity():
    state = []
    for sensor in hum_sense_list:
        state.append(pf.read_pin(sensor))
        print("reading sensor ", sensor)
        print("general state: ", pf.read())
    return state;

def pump_all():
    for pump in pump_list:
        pf.write_pin(pump, 1)
        print ("pumping " + pump)
        time.sleep(3)
        print ("stopping " + pump)
        pf.write(pump, 0)
    return
