# Handles logging of events.
# All events are logged as a row in a file
# All files starts with a timestamp... in seconds
import datetime

filename = "event_logs"


# append a row to the log.
def append_row(event_type, data):
    seconds = int((datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds())
    log_row = str(seconds) + " " + event_type + " " + str(data) + "\n"
    logs = open(filename, "a+")
    logs.write(log_row)
    logs.close()
    return


# read the entire log
def get_all_rows(event_type):
    return get_rows_between(0, 16259610920, event_type)


# get log rows in an interval
def get_rows_between(start, end, event_type):
    print "Get between " + str(start) + " and " + str(end)
    logs = open(filename, "r")
    selected_logs = []
    for log in logs:
        print "log: " + log
        print "split: " + log.split()[0]
        timestamp = float(log.split()[0])
        et = log.split()[1]
        #TODO parse out row content as object to make prettier json?
        print et
        if float(start) <= timestamp <= float(end) and (event_type is None or event_type == et):
            selected_logs.append(log)
            print "adding log " + str(timestamp)
        else :
            print "skipping log " + str(timestamp)
    return selected_logs
