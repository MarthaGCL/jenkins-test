
def game(P1, P2):
	if P1 == 'Piedra' and P2 == 'Piedra':
		return "empate"
	elif P1 == 'Tijeras' and P2 == 'Papel':
		return "P1 gana"
	elif P1 == 'Papel' and P2 == 'Piedra':
		return "P1 gana"
	elif P1 == 'Piedra' and P2 == 'Tijeras':
		return "P1 gana"
	else:
		return "P2 gana"

def main():
	op1 = raw_input("Jugador 1: ")
	op2 = raw_input("Jugador 2: ")
	print(game(op1, op2))
	
if __name__ == '__main__':
	main()