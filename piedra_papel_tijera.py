#piedra papel tijera 
option= ["piedra", "papel", "tijeras"]
def buscar_ganador(p1, p2):
    if p1 == p2:
        result = 0
    elif p1 == "piedra" and p2 == "tijeras":
        result = 4
    elif p1 == "piedra" and p2 == "papel":
        result = 2
    elif p1 == "tijeras" and p2 == "piedra":
        result = 2
    elif p1 == "tijeras" and p2 == "papel":
        result = 1
    elif p1 == "papel" and p2 == "piedra":
        result = 1
    elif p1 == "papel" and p2 == "tijeras":
        result = 2 
    return result

buscar_ganador("tijeras", "papel")

test = [["piedra","piedra", 0],["piedra","tijeras", 1],["piedra","papel",2]]

for partida in test:
    print("Jugador1 : %s - Jugador2: %s - ficha Ganadora: %s El ganador es: %s"(partida[0], partida[1], partida[2]))

from random import choice
def get_choise():
    return choice(options)

for i in range(10):
    player1 = get_choise()
    player2 = get_choise()
    print("Jugador1: %s - Jugador2 %s - Ganador: %s" %(player1, player2, buscar_ganador))
