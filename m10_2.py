import threading
from time import sleep
class knight(threading.Thread):
	def __init__(self,name='',power=1):
		threading.Thread.__init__(self)
		self.name=name
		self.power=power
	def run(self):
		print(f'{self.name}, на нас напали!')
		current_enemies=100
		days=0
		while current_enemies>0:
			sleep(1)
			days+=1
			current_enemies-=self.power
			if current_enemies<=0:
				current_enemies=0
			print(f'Рыцарь {self.name} сражается уже {days} дней, врагов осталось {current_enemies}')
		print(f'{self.name} одержал победу спустя {days} дней(дня)')


first_knight = knight('Sir Lancelot', 10)
second_knight = knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
second_knight.join()
while threading.active_count()>1:
	sleep(0.1)
print('Все бытвы закончились')