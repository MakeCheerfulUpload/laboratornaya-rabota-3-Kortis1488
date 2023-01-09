from ctypes import sizeof
import re
g = r'=-{\('
file='1'

#выбор файла
while file!='0':
    t = 0
    while t==0:
        print('выберите файл из ниже предложенных или нажмите 0 для выхода\n')
        print('test1\ntest2\ntest3\ntest4\ntest5\n')
        file = input('вводите строго как написано: ')
        print('\n\n')
        if file=='test1'or file=='test2' or file=='test3' or file=='test4' or file=='test5':
            t=1
        if file=='0':
            break
    if file=='0':
        break

    #настройка выбранного файла
    file = file+'.txt'
    file = '/home/kortis/orig/python/lab3/task1/' + file
    oFile = open(file,'r',encoding='utf-8')

    #чтение файла и подсчёт
    res = 0
    x = oFile.read()
    print('текст теста:\n')
    print(x)
    print('\n')
    res = res+len(re.findall(g,x))
    print('количество смайликов в тексте: ',res)

    #повторим?
    t = input('\nвведите "y" для продолжения, любой иной символ расценится как "нет, я не хочу продолжать": ')
    if t!='y':
       break

