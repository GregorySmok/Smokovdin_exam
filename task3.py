import csv

with open('scientist.txt', encoding='utf-8') as file:  # Откываем исходный файл
    reader = csv.reader(file, delimiter='#')
    data = list(reader)[1:]
    request = input()  # запрашиваем данные
    while request != 'эксперимент':  # программа работает пока не будет выполнено условие
        search = '-'.join([request.split('-')[2],
                          request.split('-')[1], request.split('-')[0]])  # переделываем входные данные в формат как в файле
        answer = []
        for el in data:
            if search in el:  # если искомая дата в строке, то записываем строку в список
                answer.append(el)
        if len(answer) == 0:  # проверяем, есть ли данные в списке
            print('В этот день ученые отдыхали')
        else:
            for el in answer:
                # выводим каждый элемент списка в нужном формате
                print(f'Ученый {el[0]} создал препарат: {el[1]} - {el[2]}')
        request = input()
