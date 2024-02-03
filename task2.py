import csv

with open('scientist.txt', encoding='utf-8') as file:  # Откываем исходный файл
    reader = csv.reader(file, delimiter='#')
    data = list(reader)[1:]
    # алгоритм сортировки
    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j][2] > key[2] and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    for el in data[:5]:
        print(f'{el[0]}: {el[1]}')  # выводим 5 самых ранних препаратов
