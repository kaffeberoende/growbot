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
    return logs.read()


# get log rows in an interval
def get_rows_between(start, end):
    logs = open(filename, "r")
    all_logs = logs.read()
    selected_logs = ""
    for log in all_logs:
        timestamp = datetime.datetime.fromtimestamp(log.split()[0])
        if timestamp >= start & timestamp <= end:
                selected_logs += log;
    return selected_logs
