from datetime import timedelta
from datetime import datetime

import re

def gigasecondLife(bday):
    tdelta = timedelta(seconds=10**9)
    return bday + tdelta
    
birthday = input("In YYYY-MM-DD, please: ")
assert re.fullmatch('[0-9]{4}-[0-9]{2}-[0-9]{2}', birthday)

dparams = [int(dparam) for dparam in birthday.split("-")]
print(gigasecondLife(datetime(dparams[0], dparams[1], dparams[2])))