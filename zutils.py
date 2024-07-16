import datetime

def timestamp_to_humane(value, format='%d %B %Y'):
    value = int(value)
    return datetime.datetime.utcfromtimestamp(value).strftime(format)