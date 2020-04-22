import sys

# Дано натуральное число. 
# Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO.

# григорианский календарь, 
# год високосный, если:
    # 1) его номер кратен 4, но не кратен 100, 
    # 2) а также если он кратен 400.

def count_year(year):

    year = int(year)

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("YES")
    else:
        print("NO")

if 'test' in sys.argv:
    years = [24, 28, 80, 120, 200]
    for y in years:
        print('YEAR', y)
        count_year(str(y))

else:
    y = int(input())
    count_year(y)
