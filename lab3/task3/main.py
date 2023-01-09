from ctypes import sizeof
import re
reg = r'\w{1,}\b'
reg1 = r'[aeiouyаоуыэеёиюя]'
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
    file = '/home/kortis/orig/python/lab3/task3/' + file
    oFile = open(file,'r',encoding='utf-8')
    
     #чтение файла и подсчёт
    x = oFile.read()
    print(x,'\n\n')
    word = re.findall(reg,x)

    for i in range(0,len(word)):
        vowel = re.findall(reg1,word[i]) 
        for j in range(1,len(vowel)):
            if vowel[j-1] != vowel[j]: word[i] = ''
    for i in range(0,len(word)):
        for j in range(0,len(word)):
            if len(word[i]) < len(word[j]):
                buf = word[j]
                word[j] = word[i]
                word[i] = buf
    for i in range(0,len(word)):
        if word[i] != '':
            print(word[i])

    #повторим?
    t = input('\nвведите "y" для продолжения, любой иной символ расценится как "нет, я не хочу продолжать": ')
    if t!='y':
       break

