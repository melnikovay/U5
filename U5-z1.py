#Пользователь вводит данные о количестве предприятий,
#их наименования и прибыль за 4 квартал (т.е. 4 числа)
#для каждого предприятия. Программа должна определить среднюю прибыль
#(за год для всех предприятий) и отдельно вывести наименования предприятий,
#чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
companys = {}
quantity_comp = int(input('Введите количество предприятий', ))
#Company = namedtuple ('Company', ['name', 'p1', 'p2', 'p3', 'p4'])
s = 0
for i in range (quantity_comp):
    sname = input(str(i+1) + "-я компания: ")
    profit1 =int(input("прибыль 1 кв: "))
    profit2 =int(input("прибыль 2 кв: "))
    profit3 =int(input("прибыль 3 кв: "))
    profit4 =int(input("прибыль 4 кв: "))
    sr_profit = (profit1 + profit2 + profit3 + profit4)/4
    s += sr_profit
    companys[sname] = sr_profit
    print ('Средняя  прибыль компании', sr_profit)

sr_sr = s / quantity_comp

print("\nСредняя прибыль: %.0f. Компании с прибылью выше среднего:" % sr_sr)
for i in companys:
    if companys[i] > sr_sr:
        print(i)

print("\nСредняя прибыль: %.0f. Компании с прибылью ниже среднего:" % sr_sr)
for i in companys:
    if companys[i] < sr_sr:
        print(i)
