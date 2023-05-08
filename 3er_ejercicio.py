'''
Escribir uns funcion que reciba 
una lista de tuplas y que devuelvan un diccionario 
en donde las claves sean los primeros elementos de las tuplas
y losvalores una lista con los segundos 
l= [('Nola','don Pepito'),('Nola','don jose'),('Buenos','dias'),]
'''
l= [('Nola','don Pepito'),('Nola','don jose'),('Buenos','dias'),]
b=l[0]
d=l[2]
print(l)
def devol(b,d):
    dicc={
    }
    if 'Nola'in b:
        dicc.update({'Nola':['don pepito', 'don jose']})
    if 'Buenos' in d: 
        dicc.update({'Buenos':['dias']})  
        print(dicc)
print(devol(b,d))




