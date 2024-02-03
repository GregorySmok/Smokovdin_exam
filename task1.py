import csv

with open('scientist.txt', encoding='utf-8') as file:  # Откываем исходный файл
    reader = csv.reader(file, delimiter='#')
    data = list(reader)[1:]
    data = sorted(data, key=lambda x: x[2])  # Сортируем список всех строк
    preparations = {}
    origin = []
    for el in data:  # Пробегаем по всем строкам, добавляем в словарь значения в формате Препарат : самая ранняя дата
        if el[1] in preparations.keys():
            if el[2] <= preparations[el[1]]:
                preparations[el[1]] = el[2]
        else:
            preparations[el[1]] = el[2]
    for el in data:
        # если дата в строке совпадает с самой ранней датой для препарата - ученый настоящий
        if preparations[el[1]] == el[2]:
            origin.append(el)
    police = []
    for el in data:
        # если в сторке встретилось данное значение препарата - добавляем в список значения ФИО, дата
        if el[1] == 'Аллопуринол':
            police.append([el[0], el[2]])
    print('Разработчиками Аллопуринола были такие люди:')
    for el in police:
        # выводим все данные из списка police в заданном формате
        print(f'{el[0]}-{el[1]}')
    print(f'Оригинальный рецепт принадлежит: {police[0][0]}')

# открываем нужный файл и записываем настоящих ученых
with open('scientist_origin.txt', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='#')
    writer.writerow(['ScientistName', 'preparation', 'date', 'components'])
    writer.writerows(origin)
