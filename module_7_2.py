def custom_write(file_name='',strings=['','']):
	string_positions={}
	file=open(file_name, 'x', encoding='utf-8')
	for i in range(0,len(strings)):
		x=file.tell()
		y=i+1
		z=(y,x)
		w=strings[i]
		file.write (w+'\n')
		string_positions[z]=strings[i]
	file.close()
	return string_positions
	 
	
	
info = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']


result = custom_write('text.txt', info)
for elem in result.items():
  print(elem)