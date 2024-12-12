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


h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(0)

h2.go_to(2)