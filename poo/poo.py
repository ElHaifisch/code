import modulo

modulo.mi_provincia()

class Arbol:
	name = 'cactus'

print(Arbol().name)

x = Arbol()
print(type(x))

class Campeon:
	def __init__(self, name, type):
		self.name = name
		self.type = type

	def linea(self,ataque):
		print('linea' + self.type + ataque)


x = Campeon('urgot', 'top')
print(x.name + x.type )
x.linea(' ataco con  q')
x.name = 'jhin'
print(x.name + x.type)

del x.name 
print(x.type)

class computadora:
	def __init__(self, brand, name, so):
		self.name = name
		self.brand = brand
		self.so = so
	def powerbtn(self):
		print('''Encendiendo Computadora''' +self.name, self.brand, self.so)

laptop = computadora('lenovo', 'x390' , 'windows10')
laptop.powerbtn()

modulo.mi_provincia()