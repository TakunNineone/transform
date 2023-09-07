from dateutil.relativedelta import relativedelta
from datetime import datetime

def return_date(period,duration_type):
    period_date = datetime.strptime(period, '%Y-%m-%d').date()
    if duration_type=='startQuart':
        if period_date.month not in (3,9,12):
            date_text=str((period_date - relativedelta(months=2)).replace(day=2))
        else:
            date_text = str((period_date - relativedelta(months=2)).replace(day=1))


    elif duration_type=='startMonth':
        date_text = str((period_date.replace(day=1)))

    return date_text

        #date_text= str((period_date - relativedelta(months=int(duration) - 1)).replace(day=1))


# print(return_date('2023-08-31','startQuart'))
#print(return_date('2023-02-28','startMonth'))
# print(return_date('2023-03-31','startMonth'))
#
# """
# Данное XPath выражение возвращает дату, которая зависит от значения переменной $par:refPeriodEnd.
# Если месяц в переменной $par:refPeriodEnd равен 1, 3, 5, 7, 8, 10 или 12, то результатом будет значение $par:refPeriodEnd минус один месяц.
# В противном случае, результатом будет значение $par:refPeriodEnd минус один месяц, плюс количество дней, равное разности между 31 и днем из переменной $par:refPeriodEnd.
# """