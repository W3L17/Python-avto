user_login = "login"
user_password = "pass"

login = input("Ваш логин:")
password = input("Ваш пароль:")

if(login == user_login) and (password == user_password):
    print("open")
else:
    print("closed")