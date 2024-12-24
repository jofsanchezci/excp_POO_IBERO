#cal.py
# Calculadora basica
def suma(x,y):
	return x+y

def resta(x,y):
	return x-y

def mul(x,y):
	return x*y 


def div(x,y):
	try:
		return x/y
	except:
		return "ERROR"


num1= float(input('Ingrese el numero 1: '))
num2= float(input('Ingrese el numero 2: '))

print(div(num1,num2))
print(suma(num1,num2))
print(resta(num1,num2))
print(mul(num1,num2))
