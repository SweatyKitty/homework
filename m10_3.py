import threading
import random
from time import sleep

lock=threading.Lock()

class Bank:
	def __init__(self):
		self.balance=0
	def deposit(self):
		while self.balance<500:
			lock.acquire()
			c=random.randint(50,500)
			self.balance+=c
			print(f'Пополнение: {c}, Текущий баланс: {self.balance}')
			sleep(0.001)
		if lock.locked():
			lock.release()
				
	def take(self):
		z=0
		while z<101:
			z+=1
			c=random.randint(50,500)
			print(f'Запрос на {c}')
			if c<=self.balance:
				self.balance-=c
				print(f'Снятие: {c}, баланс: {self.balance}')
			else:
				print(f'Запрос отклонен, недостаточно средств')
				lock.acquire()
				break
				
bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()