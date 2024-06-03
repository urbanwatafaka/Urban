my_list = ['apple', 'banana', 'kiwi', 'guawa', 'grapefruit']
print('Список: ', my_list)
print('Первый и последний элемент списка:',my_list[0], my_list[-1], sep=',')
print('С первого по пятый элемент списка: ',my_list[2:5])
my_list[2] = 'mango'
print('Изменение  значения для 3 элемента списка: ',my_list)

my_dict = {'sep': 'разделитель', 'end': 'перенос строки', 'цикл while': 'что-то непонятное', 'Антон': 'Ученик'}
print('Словарь: ',my_dict)
print('Значение ключа "sep": ',my_dict.get('sep'))
my_dict['sep'] = 'ну точно же sep'
print('Изменение значения ключа "sep": ',my_dict)
my_dict.update({'if':'если'})
print('Добавление нового ключа и значения в словарь: ',my_dict)
