import time as t

class urtube:
		
	def __init__(self):
		self.data={'guest':0}
		self.date={'guest':0}
		self.current_user='guest'
		self.videos={}
		
	def log_in(self,nickname,password):
		if nickname in self.data.keys():
			if self.data[nickname]==password:
				self.current_user=nickname
			else:
				print('Пользователя с такой комбинацией данных логин-пароль нет в системе')
		else:
			print('Пользователя с таким никнеймом нет в системе')
		
	def register(self,nickname,password,age=0):
		if nickname in self.data.keys():
			print('Данный пользователь уже зарегистрирован в системе')
		else:
			self.data[nickname]=password
			self.date[nickname]=age
			print('Вы успешно зарегистрированы!')
			self.current_user=nickname
		
	def log_out(self):
		print('Вы вышли из своего аккаунта')
		self.current_user='guest'
		
	def add_video(self,*args):
		for i in args:
			if isinstance(i, video):
				if i.title in self.videos.keys():
					print('Данное видео уже есть на сервере')
					continue
				else:
					self.videos[i.title]=i
			else:
				print('То, что вы пытаетесь загрузить - не видео')
				continue
			
	def get_videos(self,searchword=''):
		slist=[]
		for i in self.videos.keys():
			print(i)
			continue
#			d=str(i).upper
#			if searchword.upper in :
#			slist.uppend(i)
#			else:
#				continue
		print(slist)
		return(slist)
				
		
	def watch_video(self,watchtitle):
		if self.current_user=='guest':
			print('Вы не авторизованы в системе')
		else:
			if watchtitle in self.videos.keys():
				if self.videos[watchtitle].adult_mode==True:
					if self.date[self.current_user]<18:
						print('Упс, похоже на видео установлены возрастные ограничения')
					else:
						for i in range(1,self.videos[watchtitle].duration):
							print(i)
							self.videos[watchtitle].time_now=i
							t.sleep(1)
							if i==self.videos[watchtitle].duration-1:
								print(self.videos[watchtitle].duration)
								print('Конец видео')
								self.videos[watchtitle].time_now=i
		
		
class video:
	def __init__(self,title='',duration=0,time_now=0,adult_mode=False):
		self.title=title
		self.duration=duration
		self.time_now=0
		self.adult_mode=adult_mode
		
class user:
	def __init__(self,nickname,password,age):
		self.nickname=nickname
		self.password=hash(password)
		self.age=age

#Не сказано в задаче надо ли добавлять цикл, для работы в приложении через консоль вывода
ur=urtube()
v1=video('Лучший язык программирования 2024 года',200)
v2=video('Для чего девушкам парень-программист',10,adult_mode=True)
ur.add_video(v1,v2)
#print(ur.videos)
print(ur.get_videos('Лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.get_videos('ПРОГАаА'))
ur.watch_video('Для чего девушкам парень-программист')
ur.register('vasya_pupkin','lolkekcheburek',13)
ur.watch_video('Для чего девушкам парень-программист')
ur.register('urban_pythonist','iScX4vIJClb9YQavjAgF',25)
ur.watch_video('Для чего девушкам парень-программист')
ur.register('vasya_pupkin','F8098fzbfdzva')
print(ur.current_user)
ur.watch_video('Дasd;lvkvmf')
