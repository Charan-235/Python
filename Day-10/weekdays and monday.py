import calendar
from datetime import datetime
m, y = 8, 2024
cal = calendar.Calendar()
wee = [0] * 7
mon = None
for day, wd in cal.itermonthdays2(y, m):
    if day:
        wee[wd] += 1
        if wd == 0 and mon is None:
            mon = datetime(y, m, day)
tow = sum(wee[:5]) 
print(f"Total number of weekdays: {tow}")
print(f"Date of the first Monday: {mon.strftime('%Y-%m-%d') if mon else 'None'}")
