'''Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии'''


name = ['Alex', 'Tom', 'Ernest']
salary = [30_000, 80_000, 45_000]
bonus = [10.25, 14, 12.4]
mydict_comp = {name[i]: salary[i] * bonus[i] / 100 for i in range(len(name))}
for item in mydict_comp.items():
    print(item)