#date and time

from datetime import date, datetime, timedelta

#дата на сегодня
dt_now = datetime.now()
print(dt_now)  

dt_today = datetime.today()
print(dt_today)

#создание даты
dt2 = datetime(2015, 5, 16, 8, 3, 44)

print(dt_now.year) 
print(dt_now.month)
print(dt_now.day)

#разница дат
delta = dt_now - dt2
print(delta)
