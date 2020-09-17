a = input('Введите пароль: ')
result = 0

try:
    result = int(a) + len()
except ValueError:
    print('Вы ввели пустой пароль.')
except TypeError:
    print('Ваш пароль состоит только из цифр') 
except:
    print('Требования к паролю соблюдены')


#Задача: написать программу проверяющую введенный пользователем пароль на наличие цифр.

#Требования:

#Пользователю должно выдаваться сообщение с просьбой ввести пароль: "Введите пароль: ";
#Если пароль пустой, то должно выдаваться сообщение: "Вы ввели пустой пароль";
#Если пароль состоит только из цифр, то должно выдаваться сообщение: "Ваш пароль состоит только из цифр";
#В противном случае должно выдаваться сообщение: "Требования к паролю соблюдены".
#Реализовать программу только с использованием конструкции try/except