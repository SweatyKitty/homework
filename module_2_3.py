my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a=len(my_list)#Переменная для счета макс границы повторений
b=0#Переменная для текущего элемента списка
while my_list[b]>-1 and b!=a:
    if my_list[b]==0:
        b=b+1
        continue
    print(my_list[b])
    b=b+1
