from datetime import date
from datetime import timedelta
from calendar import monthrange

global months
global days
global subdays
global ordin

months = {
'January':1
, 'February':2
, 'March':3
, 'April':4
, 'May':5
, 'June':6
, 'July':7
, 'August':8
, 'September':9
, 'October':10
, 'November':11
, 'December':12
}

days = {
'Monday':0
, 'Tuesday':1
, 'Wednesday':2
, 'Thursday':3
, 'Friday':4
, 'Saturday':5
, 'Sunday':6
}

subdays = {
'mon':0
, 'tue':1
, 'wed':2
, 'thu':3
, 'fri':4
, 'sat':5
, 'sun':6
}

ordin = {
'first':1
, 'second':2
, 'third':3
, 'fourth':4
, 'fifth':5
}

def meetupDate(desc):
    kwrd = desc.split(' ')
    if len(kwrd) == 6 and kwrd[1] != 'last':
        baseDate = date(int(kwrd[-1]), months[kwrd[-2]], 1)
        tmpDiff = baseDate.weekday() - days[kwrd[2]]
        actDiff = ordin[kwrd[1]]*7 + 1 - tmpDiff if tmpDiff>0 else (ordin[kwrd[1]]-1)*7 - tmpDiff
    elif len(kwrd) == 6 and kwrd[1] == 'last':
        lastDay = monthrange(int(kwrd[-1]), months[kwrd[-2]])
        baseDate = date(int(kwrd[-1]), months[kwrd[-2]], lastDay[1])
        tmpDiff = baseDate.weekday() - days[kwrd[2]]
        actDiff = - tmpDiff if tmpDiff>=0 else -7 - tmpDiff
    else:
        baseDate = date(int(kwrd[-1]), months[kwrd[-2]], 15)
        actDiff = (baseDate.weekday() - subdays[kwrd[1][:3]]) + (4 - baseDate.weekday())
    return baseDate + timedelta(days=actDiff)
    
desc = 'The wednesteenth of January 2018'
print(meetupDate(desc))

ndisc = 'The fifth Monday of January 2018'
print(meetupDate(ndisc))

ndesc = 'The last Friday of February 2018'
print(meetupDate(ndesc))