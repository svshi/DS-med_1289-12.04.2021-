a = float(input("Введите значение выручки: "))
b = float(input("Введите значение издержек: "))
if a > b:
    print("Фирма работает с прибылью. Рентабельность выручки составляет: ", a / b)
    c = int(input("Введите количество сотрудников фирмы: "))
    print('Прибыль на одного сотрудника составляют: ', a / c)
elif a == b:
    print('Фирма работает в ноль.')
else:
    print('Фирма работает в убыток')