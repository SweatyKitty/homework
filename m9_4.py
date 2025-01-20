from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x,y: x==y,first,second)))


def get_advanced_writer(file_name):
	file=file_name
	def write_everything(*data_set):
		for i in data_set:
			with open(file,'a', encoding='utf-8') as f:
				if isinstance(i,str) or isinstance(i,float):
					f.write(i+' ')
				elif isinstance(i,int):
					f.write(str(i)+' ')
				else:
					for y in i:
						if isinstance(y,int):
							f.write(str(y)+' ')
						else:
							f.write(y+' ')
				
	return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
	words=[]
	def __init__(self,*args):
		for i in args:
			self.words.append(i)
	def __call__(self):
		return choice(self.words)
		
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())