from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# Парсинг даты из строки
dt = datetime.strptime('30/08/2018', '%d/%m/%Y')
print(dt)

dt = datetime.strptime('29/03/2018 10:40', '%d/%m/%Y %H:%M')
print(dt)

dt = datetime.strptime('06-28-2018 09:20', '%m-%d-%Y %H:%M')
print(dt)

dt = datetime.strptime('2018-06-28', '%Y-%m-%d')
print(dt)

# Конвертирование даты в строку
import locale
# Изменение настройки локали на Russian_Russia.1251
locale.setlocale(locale.LC_ALL, '') 

now = datetime.now()
print(now.strftime('%Y-%m-%d (%a)'))
print(now.strftime('%Y %B %d число (%A)'))

# Работа с timedelta
delta1 = timedelta(days = 3, hours = 2, minutes = 10)
print(delta1)

delta2 = timedelta(days = 2, hours = 1, minutes = 5)
print(delta1 - delta2)
print(delta2 - delta1)

my_birthday = date(1988, 8, 12)

delta = date.today() - my_birthday
print(type(delta))

my_age = int(delta.days / 365)
print(my_age)

wife_birthday = date(1990, 9, 6)

am_i_older = my_birthday < wife_birthday
print(am_i_older)