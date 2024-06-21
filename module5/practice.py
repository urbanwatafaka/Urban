class Human:
    head = True

class Student(Human):
    def about(self):
        print('Я студент')
human = Human()
student = Student()
print(student.head)