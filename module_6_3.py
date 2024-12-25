import random
import math
class animal:
	live=True
	sound=None
	_DEGREE_OF_DANGER=0
	_cords=[0,0,0]
	speed=0
	
	def __init__(self,speed=10):
		self.speed=speed
		
	def move(self,dx=1,dy=1,dz=1):
		self._cords[0]=dx*self.speed
		self._cords[1]=dy*self.speed
		if dx*self.speed<0:
			print('its too deep,  icant dive in')
		else:
			self._cords[2]=dz*self.speed
		print(self._cords)
		
	def get_cords(self):
		for i in range(0,3):
			b={0:'x',1:'y',2:'z'}
			print(f'{self._cords[i]} - координаты по {b[i]}')
			
	def attack(self):
		if self._DEGREE_OF_DANGER<5:
			print('Sorry, im peaceful')
		else:
			print('Be careful, im attacking you 0_0')
			
	def speak(self):
		print(self.sound)
		
class bird(animal):
	beak=True
	def lay_eggs(self):
		print(f'here are {random.randint(1,4)} eggs for you')
		
class aquaticanimal(animal):
	_DEGREE_OF_DANGER=3
	
	def dive_in(self,dz):
		delta=dz/2
		super()._cords[2]=int(delta*super().speed)
		
class poisonousanimal(animal):
	_DEGREE_OF_DANGER=8
	
class	Duckbill(poisonousanimal,bird,aquaticanimal):
	sound='click-click-click'
	
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()