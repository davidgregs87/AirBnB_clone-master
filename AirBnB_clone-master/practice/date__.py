#!/usr/bin/python3

import datetime

d = datetime.date(2014, 12, 22)
print(d)


tday = datetime.date.today() # this gives the date only
# tday = datetime.datetime.now() # this give the date and time
print(tday, tday.day, tday.month, tday.year)
print(tday.weekday())
print(tday.isoweekday())

# regular => Monday 0 Sunday 6
# iso		=> Monday 1 Sunday 7


tday = datetime.date.today() # this gives the date only
tdelta = datetime.timedelta(days=7)

print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2023, 9, 27)
till_bday = bday - tday
print(till_bday)

t = datetime.time(9, 30, 45, 100000)
print(t.hour)
