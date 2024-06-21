class User:
    """Пользователь вводит
    Логин
    Пароль
    Подтверждение пароля
    Возраст"""
    def __init__(self, login, password,password_confirm):
        self.login = login
        if password == password_confirm:
            self.password = password
    def login(self, login, password,password_confirm):
        self
class Database:
    def __init__(self):
        self.data = {}
    def add_user(self, login,password):
        self.data[login] = password


database = Database()
while True:
    choice = int(input('Выберете действие на клавиатуре: \n1 - Вход\n2 - Регистрация'))
    if choice ==1:
        user =
    if choice == 2:
        user = User(input('Введите логин:'), password := input('Введите пароль: '),
                    password2 := input('Повторно введите пароль: '))
        database.add_user(user.login, user.password)

        if password != password2:
            print('Вы не правильно ввели подтверждение пароля')
            exit()

