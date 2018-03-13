
from game import game

def test_game_01() :
	assert game('Piedra', 'Tijeras') == 'P1 gana', game('Piedra', 'Tijera')
	assert game('Tijeras', 'Piedra') == 'P2 gana', 'Gana jugador 2'
	assert game('Tijeras', 'Papel') == 'P1 gana', 'Gana jugador 1'

