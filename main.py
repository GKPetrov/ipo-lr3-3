day= int(input())
month= int(input)#Ввод переменных
if month>=3 and month<6 and day>0 and day<31:#Проверка на весну
    print('spring')
elif month>=6 and month<9 and day>0 and day<31:#Проверка на лето
    print('summer')
elif month>=9 and month<12 and day>0 and day<31 :#Проверка на осень
    print('Autumn')
elif month>=12 and month<3 and day>0 and day<31:#Проверка на зиму
    print('Winter')
elif month==12 and month >28:#Обработка исключений для февраля
    print('Eror')
else:#Отработка исключений если месяц не существует
    print('Такого месяца не существует')