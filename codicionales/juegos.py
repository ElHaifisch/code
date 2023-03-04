from random import randint
options = ['Piedra', 'Papel' , 'Tijera']
on = True
while on == True: 

	computer = options[randint(0,2)]
	player = input('piedra papel tijera: ')
	if player == computer:
		print("Empate")
	elif player == "Piedra":
		if computer == "Papel":
			print("Perdiste! ", computer, " > ", player)
		else:
			print("Ganaste !", player, " < ", computer)
	elif player == "Papel":
			if computer == "Tijera":
				print("Perdiste! ", computer, " > ", player)
			else:
				print("Ganaste! ", player, " < ", computer)
	elif player == "Tijera":
				if computer == "Piedra":
					print("Perdiste! ", computer, " > ", player)
				else:
					print("Ganaste! ", player, " < ", computer)
	elif player == 'Salir':
		break

	else:
		print("Error - Opción no valida, Intenta escribir las opciones como las vez.")




