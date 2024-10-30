#task2
from tkinter.ttk import Treeview

my_dict={'Yaroslav':1998,'Yulia':2000,}
print('Dict: ',my_dict)
print('Existing value: ',my_dict['Yaroslav'])
print('Not existing value: ',my_dict.get('Jaroslav'))
my_dict.update({'Mihail':1999,'Nikolya':2001})
a=my_dict.pop('Yaroslav')
print('Deleted value: ',a)
print('Modified dictionary: ',my_dict)
#task3
my_set={1,2,3,3,3,4,5,5,True,False,True,'Shade','Shade'}
print('Set:',my_set)
my_set.add(6)
my_set.add(7)
my_set.discard(3)
print('Modified set:',my_set)