
import datetime


def what_day(day, month, year):
    days = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]
    a = (14 - month) // 12
    y = year - a
    m = month + 12 * a - 2
    result = (((day + y + y // 4 - y // 100 + y // 400 + (31 * m) // 12)) % 7) - 1
    return days[result]

#print(what_day(23,7,1988))

def calc_delay_date(dispatch_date_docs, delay_in_days, type_of_days):
    #True = holiday
    list_of_dates = []

    if type_of_days == "calend":
        for i in range(0, delay_in_days):
#для реализации рабочих дней необходимо фор переписать на вайл и использовать дополнительный инкримент, каждый раз когда встречается выходной
            list_of_dates.append([dispatch_date_docs + datetime.timedelta(days=i)])
            short = what_day(list_of_dates[i][0].day, list_of_dates[i][0].month, list_of_dates[i][0].year)
            if short == "сб" or short == "вс":
                list_of_dates[i].append(True)
            elif (list_of_dates[i][0] == datetime.date(2019, 1, 1) or list_of_dates[i][0] == datetime.date(2019, 1, 2) or list_of_dates[i][0] == datetime.date(2019, 1, 3) or
            list_of_dates[i][0] == datetime.date(2019, 1, 4) or list_of_dates[i][0] == datetime.date(2019, 1, 7) or list_of_dates[i][0] == datetime.date(2019, 1, 8) or
            list_of_dates[i][0] == datetime.date(2019, 3, 8) or list_of_dates[i][0] == datetime.date(2019, 5, 1) or list_of_dates[i][0] == datetime.date(2019, 5, 2) or
            list_of_dates[i][0] == datetime.date(2019, 5, 3) or list_of_dates[i][0] == datetime.date(2019, 5, 9) or list_of_dates[i][0] == datetime.date(2019, 5, 10) or
            list_of_dates[i][0] == datetime.date(2019, 6, 12) or list_of_dates[i][0] == datetime.date(2019, 11, 4)):
                list_of_dates[i].append(True)
            else:
                list_of_dates[i].append(False)
        #прибавляем дни если выпал обычный выходной(не праздничный)
        if list_of_dates[-1][1] == True:
            list_of_dates.append([list_of_dates[-1][0] + datetime.timedelta(days=1)])
            short = what_day(list_of_dates[-1][0].day, list_of_dates[-1][0].month, list_of_dates[-1][0].year)
            if short == "сб" or short == "вс":
                list_of_dates[-1].append(True)
        #повторяем на случай воскресенья
        if list_of_dates[-1][1] == True:
            list_of_dates.append([list_of_dates[-1][0] + datetime.timedelta(days=1)])
            short = what_day(list_of_dates[-1][0].day, list_of_dates[-1][0].month, list_of_dates[-1][0].year)
            if short == "сб" or short == "вс":
                list_of_dates[-1].append(True)

    #print(list_of_dates)
    if type_of_days == "work":
        i = 0
        while i < delay_in_days:
            list_of_dates.append([dispatch_date_docs + datetime.timedelta(days=i)])
            short = what_day(list_of_dates[i][0].day, list_of_dates[i][0].month, list_of_dates[i][0].year)
            if short == "сб" or short == "вс":
                list_of_dates[i].append(True)
                delay_in_days += 1
            elif (list_of_dates[i][0] == datetime.date(2019, 1, 1) or list_of_dates[i][0] == datetime.date(2019, 1, 2) or list_of_dates[i][0] == datetime.date(2019, 1, 3) or
            list_of_dates[i][0] == datetime.date(2019, 1, 4) or list_of_dates[i][0] == datetime.date(2019, 1, 7) or list_of_dates[i][0] == datetime.date(2019, 1, 8) or
            list_of_dates[i][0] == datetime.date(2019, 3, 8) or list_of_dates[i][0] == datetime.date(2019, 5, 1) or list_of_dates[i][0] == datetime.date(2019, 5, 2) or
            list_of_dates[i][0] == datetime.date(2019, 5, 3) or list_of_dates[i][0] == datetime.date(2019, 5, 9) or list_of_dates[i][0] == datetime.date(2019, 5, 10) or
            list_of_dates[i][0] == datetime.date(2019, 6, 12) or list_of_dates[i][0] == datetime.date(2019, 11, 4)):
                list_of_dates[i].append(True)
                delay_in_days += 1
            else:
                list_of_dates[i].append(False)
            i += 1

    return list_of_dates[-1][0]





#TEST BLOCK

print(calc_delay_date(datetime.date(2019, 1, 1), 15, "calend"))
print(calc_delay_date(datetime.date(2019, 1, 1), 15, "work"))

print(calc_delay_date(datetime.date(2019, 1, 1), 19, "calend"))#проверка выпадания на выходной





