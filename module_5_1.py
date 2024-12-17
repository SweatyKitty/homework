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
        if self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False
    def __it__(self,other):
        if self.number_of_floors < other.number_of_floors:
            return True
        else:
            return False
    def __le__(self,other):
        if self.number_of_floors <= other.number_of_floors:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.number_of_floors>other.number_of_floors:
            return True
        else:
            return False
    def __ge__(self,other):
        if self.number_of_floors>=other.number_of_floors:
            return True
        else:
            return False
    def __ne__(self,other):
        if self.number_of_floors!=other.number_of_floors:
            return True
        else:
            return False
    def __add__(self,value):
        self.number_of_floors+=value
        return self.number_of_floors
    def __radd__(self,value):
        return add(self,value)
    def __iadd__(self,value):
        return add(self,value)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(0)
h2.go_to(2)

# Следующее задание module_5_2 тоже выполнено здесь

h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

print(h3.__str__())
print(len(h3))
print(str(h3))
print(len(h4))