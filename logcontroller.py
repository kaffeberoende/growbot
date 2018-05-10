# Handles logging of events.
# All events are logged as a row in a file
# All files starts with a timestamp... in seconds
import datetime

filename = "event_logs"


# append a row to the log.
def append_row(event_type, data):
    seconds = (datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds()
    log_row = str(seconds) + " " + event_type + " " + str(data) + "\n"
    logs = open(filename, "a+")
    logs.write(log_row)
    logs.close()
    return


# read the entire log
def get_all_rows():
    logs = open(filename, "r")
    return logs.readlines()


# get log rows in an interval
def get_rows_between(start, end):
    print "Get between " + str(start) + " and " + str(end)
    logs = open(filename, "r")
    selected_logs = []
    for log in logs:
        print "log: " + log
        print "split: " + log.split()[0]
        timestamp = float(log.split()[0])
        if float(start) <= timestamp <= float(end):
            selected_logs.append(log)
            print "adding log " + str(timestamp)
        else :
            print "skipping log " + str(timestamp)
    return selected_logs
