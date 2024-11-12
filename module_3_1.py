calls=0
def count_calls():
    global calls
    calls=calls+1
    print('Вызовов функций: ',calls)
    #Вариант с вводом переменной через консоль до 40й строки
def string_info():
    global calls
    calls=calls+1
    a=input("Введите данные: ")
    print((len(a), a.upper(),a.lower()))
def is_contains():
    global calls
    calls=calls+1
    a=input('Введите искомое слово: ')
    a=a.upper()
    search_list=[]
    while True:
        b=input('Введите слово для поиска \n (пустая строка для начала поиска по уже заанным словам): ')
        if b!='':
            b=b.upper()
            search_list.append(b)
        else:
            break
    print(a)
    print(search_list)
    for i in range(len(search_list)):
        if search_list[i].__contains__(a)==True:
            print('True')
            break
        else:
            if i==len(search_list)-1:
                print('False')
                break
            continue
string_info()
string_info()
is_contains()
is_contains()
count_calls()
#Вариант как написано в примере выполнения кода
#Для проверки - закомментить строки 36-40чтобы не мешали
# а строки 61-69 откомментить
def string_info_0(a=''):
    global calls
    calls = calls +1
    b=(len(a),a.upper(),a.lower())
    return(b)
def is_contains_0(a='',b=['']):
    global calls
    calls = calls + 1
    a=a.upper()
    for i in range(len(b)):
        b[i]=b[i].upper()
        if b[i].__contains__(a)==True:
            return('True')
        else:
            if i==len(b)-1:
                return('False')
            continue
# print(string_info_0('Capybara'))
#
# print(string_info_0('Armageddon'))
#
# print(is_contains_0('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
#
# print(is_contains_0('cycle', ['recycling', 'cyclic'])) # No matches
#
# print(calls)