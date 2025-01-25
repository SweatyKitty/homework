import os
from time import sleep, time
import threading

def check_before_write(func):
	def wrapper(*args):
		path=os.getcwd()
		for i in args:
			if isinstance(i, str):
				if os.isfile(i)==False:
					new_file=open(i,'x',encoding='utf-8')
					new_file.close
				else:
					pass
			else:
				continue
		t=time()
		res=func(*args)
		t=time()-t
		print(f'Функция выполнена за {t}')
		return res
	return func

@check_before_write
def write_words(word_count, file_name):	
	t=time()
	with open(file_name, 'a',encoding='utf-8') as file:
		for i in range(1,word_count+1):
			#print(f'запись в {file_name} поток {threading.current_thread()}')
			file.write(f'Какое-то слово No {i}\n')
			sleep(0.1)
	print(f'Функция выполнена за {time()-t}')
	print(f'Завершилась запись в файл {file_name}')


t_example=time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
print(f'Работа основного потока при последовательном выполнеиисоставила: {time()-t_example}')
		
t1_task=(10, 'example5.txt')
t2_task=(30, 'example6.txt')
t3_task=(200, 'example7.txt')
t4_task=(100, 'example8.txt')

t1=threading.Thread(target=write_words,args=t1_task)
th_ti=time()
t1.start()
t2=threading.Thread(target=write_words,args=t2_task)
t2.start()
t3=threading.Thread(target=write_words,args=t3_task)
t3.start()
t4=threading.Thread(target=write_words,args=t4_task)
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
print(f'Работа при одновременном выполнении на разных потоках составила: {time()-th_ti}')