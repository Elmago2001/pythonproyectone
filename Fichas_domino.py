'''7. Escribir una funcion que indique si dos fichas de domino encajan o no. Las fichas son recibidas
en dos tuplas, por ejemplo: (3,4) y (5,4).'''

def encajan():
    ficha1 = tuple(map(int, input("Introduce los números de la primera ficha separados por espacios: ").split()))
    ficha2 = tuple(map(int, input("Introduce los números de la segunda ficha separados por espacios: ").split()))

    if (ficha1[0] == ficha2[0] or ficha1[1] == ficha2[1] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0]):
        print("Las fichas encajan.")
    else:
        print("Las fichas no encajan.")

encajan()