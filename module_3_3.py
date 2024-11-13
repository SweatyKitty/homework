from traceback import print_exc


def print_params(a=1,b='строка',c=True):
    print(a,b,c)
print_params()
print_params(4,4,4)
print_params(b = 25)
print_params(c = [1,2,3])

values_list=[1,True,'string']
values_dict={'a':2,'b':False,'c':'dictionary'}

print_params(*values_list)
print_params(**values_dict)
values_list_2=[5.32,True]
print_params(*values_list_2,42)