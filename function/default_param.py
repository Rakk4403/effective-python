# author: rakk4403@gmail.com
import datetime
import json


# good case
def log(message, when=None):
    """Log a message with a timestamp

    @param message: message to print
    @param when: datetime, default to present time
    """
    when = datetime.now() if when is None else when
    print('%s: %s' % (when, message))


# bad case
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


# fixed case
def fixed_decode(data, default=None):
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default
