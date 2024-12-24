class vehicle:
	owner=''
	__model=''
	__engine_power=0
	__color=''
	__color_variants=['red','blue','yellow','white','black']
	def get_model(self):
		return(self._vehicle__model)
	def get_horsepower(self):
		return(self.__engine_power)
	def get_color(self):
		return(self.__color)
	def print_info(self):
		print(self.get_model())
		print(self.get_horsepower())
		print(self.get_color())
		print(f'Владелец: {self.owner}')
	def set_color(self,new_color=''):
		y=False
		for i in range(0,len(self.__color_variants)-1):
			j=str(self.__color_variants[i])
			#print(j.capitalize)
			if new_color.upper==j.upper:
				y=True
				self.__color=new_color
				print(f'Вы Успешно измнили цвет авто на {new_color}')
				break
			else:
				continue
		if y==False:
			print(f'Нельзя сменить цвет на {new_color}')
class sedan(vehicle):
	def __init__(self,owner='',model='',color='',engine_power=0):
		self.owner=owner
		self._vehicle__model=model
		self._vehicle__color=color
		self._vehicle__engine_power=engine_power
	__passengers_limit=5
	
v1=sedan('Fedos','Toyota Mark II','blue',500)
#print(dir(v1))
v1.print_info()
v1.set_color('PINk')
v1.set_color('BLACK')
v1.owner='Vasyok'
v1.print_info()