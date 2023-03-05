def mi_funcion():
	print('mi primera funcion')

mi_funcion()

def universo(planeta):
	print('El el universo esta: ' + planeta)

universo('pluton')
universo('marte')
universo('jupiter')


def planeta(p):
	p = input('planeta: ') 
	if p == 'pluton' :
		print('Mi planeta favorito')
	else :
		print('No me gusta')

planeta('A')

def formula_velocidad(d,t):
	v= d/t 
	print(v)

formula_velocidad(10, 1)