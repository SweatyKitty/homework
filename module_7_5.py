import os
import time
directory=os.getcwd()
#print(directory)
#print(os.listdir(directory))
d=[]
def print_files_info(path):
	for i in os.listdir(path):
		if os.path.isfile(i):
			print(i)
		else:
			continue

print_files_info(directory)
for y in os.listdir(directory):
	if os.path.isdir(y):
		print(y)
		path_1=directory+f'/{y}'
		print_files_info(path_1)
	else:
		continue
		
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(directory, os.path.dirname(file))
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize =os.path.getsize(filepath)
    parent_dir = os.path.dirname(file)
    print(f'Обнаружен файл: {file}, Путь: {filepath}{file}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')