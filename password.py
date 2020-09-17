a = input('Введите пароль: ')

try:
    result = int and str(a)
except TypeError:
    print('Ваш пароль состоит только из цифр') 
except ValueError:
    print('Вы ввели пустой пароль.')
except:
    print('Требования к паролю соблюдены')
