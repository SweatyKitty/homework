class animal:
	def __init__(self,name):
		self.alive=True
		self.fed=False
		self.name=name
	def eat(self,food):
		if isinstance(food, plant)==True:
			if food.edible==True:
				print(f'{self.name} съел {food.name} и наелся')
				self.fed=True
			else:
				print(f'{self.name} не стал есть {food.name} и умер')
				self.alive=False
		
class plant:
	def __init__(self,name):
		self.edible=False
		self.name=name
	
class mammal(animal):
	pass
class predator(animal):
	pass
	
class flower(plant):
	pass
class fruit(plant):
	def __init__(self,name):
		self.edible=True
		self.name=name

a1=predator('Волк с Уолл-стрит')
a2=mammal('Хатико')
p1=flower('Цветик-семицветик')
p2=fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)