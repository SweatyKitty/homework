def is_prime(func):
	def wrapper(*args):
		b=0
		for i in args:
			b+=i
		if b in range(0,9):
			print('Простое')
		else:
			print('Составное')
		return b
	return wrapper

@is_prime	
def sum_three(num1=0,num2=0,num3=0):
	res=num1+num2+num3
	return res

result=sum_three(2,3,3)
print(result)