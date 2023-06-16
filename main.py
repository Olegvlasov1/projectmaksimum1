def palindrom(a):
    if a == a[::-1]:
        print('True')
    else:
        print('False')
a = input('Введите палиндром')
palindrom(a)