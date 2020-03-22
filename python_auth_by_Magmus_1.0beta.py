# version: 1.0beta
print ("Register\n")
login_save = input("Введите желаемое имя: ")
while login_save.__sizeof__ () > 45:
    login_save = input("Ваш логин весит более ста байт. Пожалуйста, сделайте его меньше: ")
    
if login_save != "test":
    password_save = input("Введите желаемый пароль: ")
    while password_save.__sizeof__ () < 34:                                                                                     # and password_save.__sizeof__ () < 36:
        password_save = input("Ваш пароль слишком легкий. Пожалуйста, сделайте его сложнее: ")
    psswrd_check = input ("Повторите пароль: ")
    #if !!!!ЗАБЫЛ ЧТО ХОТЕЛ ЖОБАВИТЬ!!!

    if psswrd_check == password_save:
        print("Регистрация завершена\n\n")
        while psswrd_check != password_save:
            psswrd_check = input ("Вы повторили пароль неверно. Попробуйте еще раз: " )
            if psswrd_check == password_save:
                print("\nРегистрация прошла успешно\n")
else:
     print("Вы вошли в систему как тестер!")
     password_save="1"
     
print("login_save занимает:", login_save.__sizeof__ (), "байт")

if login_save != "test":
    print("\n\nАвторизация")
    login = input("Введите имя пользователя: \n")
    password = input("Введите пароль: ")

    if login == login_save and password == password_save:
        print("Вы успешно авторизовались")
    else:
        auth = False
        while auth != True:
            print("Пароль или логин введены неверно")
            login = input("Повторите ввод. Логин: ")
            password = input("Повторите пароль: ")
            if login == login_save and password == password_save:
                print("\nВы успешно авторизовались!")
                auth = True

adm_values ={'Creator': '123456', "Moderator": "134434", "Admin": "1234534", "Proector": "7878"}

control = ["y","n","да","нет"]

admm = input("Являетесь ли вы Администратором проекта? [y/n] или [да/нет]: ")
while admm.lower() not in control:
    admm = input("Такого ответа нет. Введите n/y или да/нет: ")

adm_check = None
# 1 = true
# 2 = False
# 3 = hz
if admm in ["y", "да"]:
    adm_auth = input("Введите логин Администратора: ")
    adm_auth in adm_values
    adm_auth_pass = input("Введите пароль от своего аккаунта Администрации: ")
    adm_auth_pass in adm_values
    if adm_auth in adm_values and adm_auth_pass == adm_values[adm_auth]:
        adm_check = True
        print("Вы успешно авторизовались как ", adm_auth)
        print("Теперь Вам доступна команда newpromocode.")
    else:
        print("Логин или пароль введены неверно!")

else:
    print ("Спасибо! Можете продолжить работу с программой")


promocodes = ["NEWWW", "Gazilka", "VIP"]
i = 0
cmds_list = ["help", "newpromocode"]
mop = 0
print("Теперь вы можете вводить что угодно. Список команд >> help")
while i == 0:
    vvod = input("Ввод: ")
     
    if vvod == ("help"):
        print("Вот все команды:\n")
        print("help - список команд")
        if adm_check == True:
            print("newpromocode - Добавляет промокод, который Вы укажите. Действует только для администрации.")
        print("stop - останавливает действие ввода")
        print("promocodes - список действующих промокодов")
        print("adm_auth - авторизоваться под именем администратора")
        if adm_check == True:
            print("admq - Выйти из аккаунта %s" % adm_auth)
         
    if vvod == ("adm_auth"):
        if adm_check == None:
            adm_auth = input("Введите логин Администратора: ")
            adm_auth in adm_values
            adm_auth_pass = input("Введите пароль от своего аккаунта Администрации: ")
            adm_auth_pass in adm_values
            if adm_auth in adm_values and adm_auth_pass == adm_values[adm_auth]:
                adm_check = True
                print("Вы успешно авторизовались как ", adm_auth)
                print("Теперь Вам доступна команда newpromocode.")
            else:
                print("Логин или пароль введены неверно!")
                yn = input("\nПовторить попытку? y/n или да/нет: ")
                if yn == "y" or yn == "да" or yn == "Y" or yn == "ДА":
                    adm_check = 0
                    while adm_check == None or adm_check == False:
                        adm_auth = input("Введите логин Администратора: ")
                        adm_auth in adm_values
                        adm_auth_pass = input("Введите пароль от своего аккаунта Администрации: ")
                        adm_auth_pass in adm_values
                        if adm_auth in adm_values and adm_auth_pass == adm_values[adm_auth]:
                            adm_check = 1
                            print("Вы успешно авторизовались как ", adm_auth)
                            print("Теперь Вам доступна команда newpromocode.")
                            
                        else:
                            yn = input("Данные введены неверно. Желаете повторить? n/нет, да - пропустить строку: ")
                            if yn == ("n") or yn == ("нет"):
                                adm_check = False
                else:
                    print("Такого ответа нет")
                        
                    
                
        else:
            print("Вы уже авторизованы!")
         

         
    if vvod == ("newpromocode"):
        if adm_check == 1:
            promo = input("Введите название промокода: ")
            promocodes.append(promo)
            yn = input("Промокод успешно добавлен. Хотите ли вы добавить еще промокоды? y/n или да/нет: ")
            while yn != control or hz != 0:
                yn = input("Такого ответа нет. Вводите верные значения!: ")
                if yn == "y" or yn == "да":
                    while mop == 0:
                        print("Напишите mop, когда захотите выйти")
                        vvod2 = input("Вводите значения: ")
                        if vvod2 == "mop":
                            mop = 2
                        if vvod2 != mop:
                            promocodes.append(vvod2)
                            
            if yn == "n" or yn == "нет":
                print("OK!")
        else:

             print("У вас нет прав на данную команду")
            
    if vvod == ("stop"):
        i = 1
    if vvod == ("promocodes"):
        print(promocodes)
    if vvod == ("admq"):
        adm_check = False
        print("Вы успешно покинули пост %s" % adm_auth)





        #Next update: 23.03.20 or 24.03.20 / ENG version (1.01beta)
