# Программа для регистрации и авторизации пользователя
LOGIN = 'login.txt'
PASSWORD = 'password.txt'
LOGIN_PASSWORD = "log_password.txt"

def creating_file():
    try:
        with open(LOGIN) as file_login:
            file_login.read()
    except FileNotFoundError:
        with open(LOGIN, 'w') as file_login:
            file_login.write('These are your files!\n')
    try:
       with open(LOGIN_PASSWORD) as file_login_password:
           file_login_password.read()
    except FileNotFoundError:
        with open(LOGIN_PASSWORD, 'w') as file_login_password:
            file_login_password.write('These are your files-passwords!\n')


def check_login_record(status_login, exclude_repetition, login, password, reg_user):
    if status_login == True and exclude_repetition == False:  # условие записи логина в файл
        save_login_password(password, reg_user) # вызов функции записи логина-пароля
        with open(LOGIN, 'a') as file:
            file.write(login + '\n')  # дозаписываем логины
    if exclude_repetition == True:
        print('Такой логин уже есть!')
    if status_login == False:  # если в переменной -ноль, логин не корректен
        print("Некорректный логин !")

def check_login(login, password, reg_user):
    status_login = 0  # объявление переменной счетчика
    exclude_repetition = 0 # пременная-счетчик повторов
    with open(LOGIN) as file:
        logins_verifieds = file.read().split('\n')
        for login_verified in logins_verifieds:  # перебираем созданный список)
            if login_verified != login and 2 < len(login) < 21:  # условия создания логина
                status_login = True
            if login_verified == login:  # проверяем логин на оригинальность
                exclude_repetition = True
    check_login_record(status_login, exclude_repetition, login, password, reg_user)


def save_login_password(password, reg_user):
    if 3 < len(password) < 36:
        with open(LOGIN_PASSWORD, 'a') as file_login_password:  # дозаписываем пару логин-пароль
            file_login_password.write(str(reg_user) + '\n')
            print("Регистрация прошла успешно!")
    else:  # иначе сообщаем о некорректном пароле
        print("Вы ввели некорректный пароль!")


def registration():  # Функция регистрации пользователя
    login = input('Придумайте себе логин: ... ')
    password = input('Придумайте пароль: ... ')
    reg_user = f'({login}/{password})'  
    check_login(login, password, reg_user)


def read_log_password(aut_user):
    search_truth = 0  # объявляем переменную счетчик
    with open(LOGIN_PASSWORD) as file_log_password:  # открываем файл с парами логин-пароль
        for login_password in file_log_password:
            if login_password == aut_user + '\n':
                search_truth = True
        file_log_password.read().split('\n')
    if search_truth == True:
        print("Авторизация пройдена успешно! Поздравляем! ")
    if search_truth == False:
        print("Вы не прошли авторизацию! Попробуйте еще раз!")


def auth():  # Функция авторизации пользователя
    login = input("Введите логин для авторизации: ... ")
    password = input("Введите пароль для авторизации: ... ")
    aut_user = f'({login}/{password})' # пара логин-пароль
    read_log_password(aut_user)


def main():  # Функция выбора регистрации или авторизации
    creating_file()
    aut_file = ''
    while aut_file != 'exit':
        aut_file = input("Регистрация - 1, Авторизация - 2: ... ").lower()
        if aut_file == 'exit':
            print('До свидания!')
        elif aut_file == "1":
            registration()
        elif aut_file == "2":
            auth()
        else:
            print("Некорректный ввод")


if __name__ == '__main__':
    main()
