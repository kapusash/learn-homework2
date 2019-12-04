"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
import datetime

def print_days():
    print(datetime.date.today())
    print(datetime.date.today() - datetime.timedelta(days=1))
    print(datetime.date.today() + datetime.timedelta(days=1))

def str_2_datetime(string):

    dt_parser = datetime.datetime.strptime(string,"%d/%m/%y %H:%M:%S.%f")
    return dt_parser

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
