class House:
    def __init__(self,name,floors):
        self.name=name
        self.number_of_floors=floors
    def go_to(self, new_floor):
        if new_floor>self.number_of_floors or new_floor<1:
            print('Такого этажа не существует')
        elif 0<new_floor<self.number_of_floors+1:
            i=0
            while i<new_floor:
                i+=1
                print(i)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.__len__()}'
    
    
    
    #MODULE_5_3
    
    
    def __eq__(self,other):
        if isinstance(other,int):
            return self.number_of_floors==other
        elif isinstance(other,House):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Ne tot class- ', type(other), other)
    def __it__(self,other):
        if isinstance(other,int):
            return self.number_of_floors<other
        elif isinstance(other,House):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Ne tot class- ', type(other), other)
    def __le__(self,other):
        if isinstance(other,int):
            return self.number_of_floors<=other
        elif isinstance(other,House):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Ne tot class- ', type(other), other)
    def __gt__(self,other):
        if isinstance(other,int):
            return self.number_of_floors>other
        elif isinstance(other,House):
            return self.number_of_floors>other.number_of_floors
        else:
            print('Ne tot class- ', type(other), other)
    def __ge__(self,other):
        if isinstance(other,int):
            return self.number_of_floors>=other
        elif isinstance(other,House):
            return self.number_of_floors>=other.number_of_floors
        else:
            print('Ne tot class- ', type(other), other)
    def __ne__(self,other):
        if isinstance(other,int):
            return self.number_of_floors!=other
        elif isinstance(other,House):
            return self.number_of_floors!=other.number_of_floors
        else:
            print('Ne tot class- ', type(other), other)
    def __add__(self,value):
        if isinstance(value,int):
            self.number_of_floors += value
            return self
        elif isinstance(value,House):
            self.number_of_floors += value.number_of_floors
            return self
        else:
            print('Ne tot class- ', type(value), value)
    def __radd__(self,value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
        else:
            print('Ne tot class- ', type(value), value)
    def __iadd__(self,value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        elif isinstance(value, House):
            self.number_of_floors += value.number_of_floors
            return self
        else:
            print('Ne tot class- ', type(value), value)

# h1 = House('ЖК Горский', 18)
# h2 = House('Домик в деревне', 2)
#
# h1.go_to(0)
# h2.go_to(2)
#
# # Следующее задание module_5_2 тоже выполнено здесь

h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

# print(h3.__str__())
# print(len(h3))
# print(str(h3))
# print(len(h4))

print('module_5_3:')
print(h3)
print(h4)
print(h3 == h4) # __eq__
h3 = h3 + 10 # __add__
print(h3)
print(h3 == h4)
h3 += 10 # __iadd__
print(h3)
h4 = 10 + h4 # __radd__
print(h4)
print(h3 > h4) # __gt__
print(h3 >= h4) # __ge__
print(h3 < h4) # __lt__
print(h3 <= h4) # __le__
print(h3 != h4) # __ne__