from pprint import pprint

class Product:
	def __init__(self,name='',weight=0.0,category=''):
		self.name=name
		self.w=weight
		self.cat=category
		
	def __str__(self):
		a=self.name
		b=str(self.w)
		c=self.cat
		d=a+', '+b+', '+c
		return d

class Shop:
	__file_name='products.txt'
	def get_products(self):
		file=open(self.__file_name,'r')
		prod_list=file.read()
		file.close()
		return(prod_list)
	def add(self,*products):
		file=open(self.__file_name,'r')
		prod_list=file.read()
		file.seek(0)
		end_id=file.read()
		#print(f'eto to samoe \n{end_id}')
		file.close()
		
		file=open(self.__file_name,'a')
		for i in products:
			d=i.name+', '+str(i.w)+', '+i.cat
			#print(f'eto to samoe \n{d}')
			if end_id.count(d)>0:
				print(f'Продукт {i.name} уже есть в магазине')
				continue
			else:
				dd='\n'+d
				file.write(dd)

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())