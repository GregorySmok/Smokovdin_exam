# Приложение для поиска препаратов
## Описание
Данное приложение позволяет искать нужные препараты, выявлять злоумышленников, крадущих идеи, искать учёных в базе и создавать личный кабинет
## Как установить и запустить проект
Проект не требует установки, вам понадобитсяЖ
- Python 3.10
- Программа-интерпретатор/текстовый редактор
## Как использовать проект
### task1.py
Работа этого файла заключается в том, чтобы удалить злоумышленников из базы и вычислить ученых, изготавливающих опасный препарат
```python
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
```
### task2.py
Этот файл сортирует имеющуюся базу по дате в порядке возрастания
```python
for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j][2] > key[2] and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
```
и выводит 5 самых ранних препаратов
