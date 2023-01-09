from ctypes import sizeof
import re
reg = r'[0-2][0-4]:[0-5][0-9]'
reg1= r'[0-2][0-4]:[0-5][0-9]:[0-5][0-9]'
file='1'
filer="f"

#набор операций
def testO():
    res = '0'
    x = oFile.read()
    print('исходный текст теста:\n')
    print(x)
    print('\n')
    res = re.sub(reg,'TBD',x)
    print('новый текст: ',res)

def testTw():
    res = 0
    x = oFile.read()
    print('исходный текст теста:\n')
    print(x)
    print('\n')
    res = re.sub(reg1,'TBD',x)
    res = re.sub(reg,'TBD',res)
    print('новый текст: ',res)
def testTh():
    res = 0
    x = oFile.read()
    print('исходный текст теста:\n')
    print(x)
    print('\n')
    res = re.sub(reg,'TBD',x)
    res = re.sub(reg1,'TBD',res)
    print('новый текст: ',res)

def testFo():
    res = 0
    x = oFile.read()
    print('исходный текст теста:\n')
    print(x)
    print('\n')
    res = re.sub(reg,'TBD',x)
    res = re.sub(reg1,'TBD',res)
    print('новый текст: ',res)

def testF():
    res = 0
    x = oFile.read()
    print('исходный текст теста:\n')
    print(x)
    print('\n')
    res = re.sub(reg,'TBD',x)
    res = re.sub(reg1,'TBD',res)
    print('новый текст: ',res)


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
    filer=file
    file = file+'.txt'
    file = '/home/kortis/orig/python/lab3/task2/' + file
    oFile = open(file,'r',encoding='utf-8')
    
    #выбор операции по выбранному тесту
    if filer == 'test1':
        testO()
    if filer == 'test2':
        testTw()
    if filer == 'test3':
        testTh()
    if filer == 'test4':
        testFo()
    if filer == 'test5':
        testF()

     #повторим?
    t = input('\nвведите "y" для продолжения, любой иной символ расценится как "нет, я не хочу продолжать": ')
    if t!='y':
       break


