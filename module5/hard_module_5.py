import time
class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password: str):
        return hash(password)

    def verify_password(self, password: str):
        return self.password == self.hash_password(password)

    def __str__(self):
        return f"Пользователь(Ник='{self.nickname}', Возраст={self.age})"


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def play(self):
        # Воспроизведение видео
        print(f"Воспроизведение видео: {self.title}")

    def stop(self):
        # Остановка видео
        print("Видео остановлено.")

    def set_time_now(self, time: int):
        # Установка текущего времени видео
        if 0 <= time <= self.duration:
            self.time_now = time
            print(f"Текущее время установлено на {self.time_now} секунд.")
        else:
            print("Неправильное время.")

    def __str__(self):
        return f"Видео(название='{self.title}', продолжительность={self.duration}, 18+={self.adult_mode})"

class UrTube:
    def __init__(self):
        self.users = []  # Список пользователей
        self.videos = []  # Список видео
        self.current_user = None  # Текущий пользователь

    def log_in(self, login: str, password: str):
        for user in self.users:
            if user.nickname == login and user.verify_password(password):
                self.current_user = user
                print(f"Пользователь {login} вошел в систему.")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f"Пользователь {nickname} успешно зарегистрирован.")
        self.current_user = new_user  # Автоматический вход после регистрации

    def log_out(self):
        self.current_user = None
        print("Пользователь вышел из системы.")

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео с названием '{video.title}' уже существует.")

    def get_videos(self, keyword: str):
        found_videos = [video.title for video in self.videos if keyword.lower() in video.title.lower()]
        return found_videos

    def watch_video(self, title: str):
        if self.current_user is None:
            print("Войдите в аккаунт чтобы смотреть видео")
            return

        found = False
        for video in self.videos:
            if title == video.title:
                found = True
                if self.current_user.age >= 18 or not video.adult_mode:
                    print(f"Просмотр видео '{video.title}' начат.")
                    for second in range(video.duration):
                        print(f"Прошло {second + 1} секунд")
                        time.sleep(1)
                    print("Конец видео")
                else:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                break

        if not found:
            print(f"Видео с названием '{title}' не найдено.")

    def __str__(self):
        return f"UrTube(Пользователей={len(self.users)}, Видео={len(self.videos)}, Текущий пользователь={self.current_user})"


# Создание объекта UrTube
ur = UrTube()

# Создание видео
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')