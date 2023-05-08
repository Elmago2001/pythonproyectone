'''5. Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por
pantalla el numero de veces que aparece la letra en la frase.'''

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

contador = 0
for caracter in frase:
    if caracter.lower() == letra.lower():
        contador += 1

print("La letra", letra, "aparece", contador, "veces en la frase.")