#!/usr/bin/python3

from datetime import date, datetime, time

today = date.today()
print(today)

print(today.strftime("%a, %dth of %b %y"))

next_year = today.replace(year = today.year + 1)
print(next_year)

difference = abs(next_year - today)
print("only {} days until next year".format(difference.days))

nikola_tesla = date(1856, 7, 10)
nikola_tesla = date.fromisoformat("1856-07-10")
print("Nikola Tesla was born on:", nikola_tesla)
print(nikola_tesla.weekday())

now = datetime.now()
print("right now it's:", now)
print("It's the {}th minute of the {}nd hour, of the {}th day of the {}nd \
month".format(now.minute, now.hour, now.day, now.month))

chernobyl = datetime.fromisoformat("1986-04-26 01:23:40:000+01:00")
print('the nuclear disaster in chernobyl occured on:', chernobyl)
print(chernobyl.strftime("The chernobyl disaster occured on %A %B %dth,\
%Y at %X MSD(%Z)"))
print("MSD is actually:", chernobyl.tzinfo)

my_time = time(15, 33, 8)
my_time = time.fromisoformat("15:33:08+01:00")
print(my_time)
print(my_time.strftime("%I:%M %p"))

my_date = date(2022, 9, 27)
my_bday = datetime.combine(my_date, my_time)
print(my_bday)
