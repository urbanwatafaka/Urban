def calculate_structure_sum(data):
    total_sum = 0

    for item in data:
        if isinstance(item, int) or isinstance(item, float): #проверяем на натуральные числа и числа с точкой
            total_sum += item
        elif isinstance(item, str): #проверяем на строки
            total_sum += len(item)
        elif isinstance(item, list) or isinstance(item, tuple) or isinstance(item, set): #проверяем на список, кортеж, множество
            total_sum += calculate_structure_sum(item)
        elif isinstance(item, dict): #проверяем на словарь
            total_sum += sum(len(key) for key in item.keys()) + calculate_structure_sum(item.values())

    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
