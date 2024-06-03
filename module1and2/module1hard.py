#Дано:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}

#Вычисляем среднюю оценку в каждом подсписке
first_podspisok = sum(grades[0]) / len(grades[0])
second_podspisok = sum(grades[1]) / len(grades[1])
third_podspisok = sum(grades[2]) / len(grades[2])
four_podspisok = sum(grades[3]) / len(grades[3])
five_podspisok = sum(grades[4]) / len(grades[4])

#Сортируем множество и превращаем его в список
sorted_students = sorted(list(students))

#Присваиваем к переменным значения по индексу из отсортированного списка
firstname, secondname, thirdname, fourname, fivename = (sorted_students[0],
                                                        sorted_students[1],
                                                        sorted_students[2],
                                                        sorted_students[3],
                                                        sorted_students[4])
#Создаем пустой словарь
count_students = {}

#Присваиваем к пустому словарю ключ и значение
count_students.update({firstname: first_podspisok})
count_students.update({secondname: second_podspisok})
count_students.update({thirdname: third_podspisok})
count_students.update({fourname: four_podspisok})
count_students.update({fivename: five_podspisok})
print(count_students)
