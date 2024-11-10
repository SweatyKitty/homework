def get_matrix(m,n,value):
    matrix=[]
    for i in range(n):
        pustoy_spisok=[]
        for x in range(m):
            pustoy_spisok.append(value)
        matrix.append(pustoy_spisok)
    return matrix
m=int(input('Введите кол-во столбцов: '))
n=int(input('Введите кол-во строк: '))
value=int(input('Введите значение: '))
a=get_matrix(m,n,value)
print(a)