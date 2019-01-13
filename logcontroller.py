# Handles logging of events.
# All events are logged as a row in a file
# All files starts with a timestamp... in seconds
import datetime

import sqlite3
import time

filename = "event_logs"
number_of_sensors = 2 #TODO keep somewhere else


# add a moisture reading to the log.
def store_moisture(sensor, sensor_state):
    print "storing moisture ", sensor_state, " for sensor ", sensor

    conn = sqlite3.connect('growbot.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO moisture VALUES((?), (?), (?))", (time.time(), sensor, sensor_state))
    conn.commit()
    print "inserted moisture"


# add a weather reading to the log.
def store_weather(weather_reading):
    print "storing weather ", weather_reading


# add a pump event to the log.
def store_pump_event(pump, event):
    print "storing pump event for ", pump
    conn = sqlite3.connect('growbot.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO pump_events VALUES((?), (?), (?))", (time.time(), pump, event))
    conn.commit()
    print "inserted pump event"


# get the latest moisture values for all active sensors.
def get_latest_moisture():
    print "Getting the latest moisture"
    return get_moisture_between(0, time.time(), number_of_sensors)


# get log moisture values in an interval
def get_moisture_between(start, end, limit = -1):
    print "Get between " + str(start) + " and " + str(end)

    conn = sqlite3.connect('growbot.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM moisture WHERE time >= ? AND time <= ? LIMIT ?", (start, end, limit))
    selected_logs = curs.fetchall()
    return selected_logs
