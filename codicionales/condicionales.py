#if else

name= input('CUAL ES TU NOMBRE: ')

if name =='harold' or name=='HAROLD' or name== 'Harold':
	print('Welcome')
elif name == 'leo' :
	print('Welcome')
elif name == 'elsa' :
	print('Welcome')	

else: 
	print('NO TIENES ACCESO')

#WHILE
a= 1
while a<11:
	print(a)
	a += 1
#FOR

pokedex = ['pikachu', 'bulbasor' , 'charizard']
for pokemon in pokedex :
	print(pokemon)


