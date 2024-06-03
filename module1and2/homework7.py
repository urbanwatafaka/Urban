my_dict = {'Anton': 1996,
           'Fedor': 1998,
           'Eugen': 2000,
           'Oleg': 2002,
           'Alexandr': 1990}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Ilya'))
my_dict['Anna'] = 1992
my_dict['Oksana'] = 1973
print(my_dict)
my_dict.pop('Anna')
print(my_dict)

my_set = {1, 2.5, 'apple', (1, 2), True, 2.5}
print(my_set)
my_set.add(False)
print(my_set)
my_set.remove((1,2))
print(my_set)