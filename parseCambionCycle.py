import datetime
import re

def parseCambionJson(json_data):
    active = json_data['active'] # gets the current cycles name
    timeLeft = getCambionTime(json_data['activation'], json_data['expiry'])
    # create a new dict with active and timeLeft and return it
    cambion_dict = {
            "active": active,
            "timeLeft": timeLeft,
            }
    return cambion_dict



def getCambionTime(activation_time, expiry_time):
    tdelta = datetime.timedelta(hours=3) # plus 3 hours to get my timezone
    time_now = datetime.datetime.now()

    # convert the strings to datetime objects
    time_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    cambion_active_datetime = datetime.datetime.strptime(activation_time, time_format)
    cambion_expiry_datetime = datetime.datetime.strptime(expiry_time, time_format)

    # convert the expiry time into utc+3 timezone
    cambion_time_in_utc = cambion_expiry_datetime + tdelta

    time_diff = cambion_time_in_utc - time_now
    # format the time_diff to be usable on the website. ex. '1h 53m 23s'

    return parseExpiryTime(str(time_diff))

def parseExpiryTime(exstr):
    # take the microseconds away
    no_micro_secs = re.sub("\.\d+$", '', exstr)
    # split the string with ':'
    hour, mins, sec = no_micro_secs.split(':')
    # put it into new format
    # check if hour == 0 then dont print it
    if hour == '0':
        format_string = f"{mins}m {sec}s"
    else:
        format_string = f"{hour}h {mins}m {sec}s"

    return format_string

