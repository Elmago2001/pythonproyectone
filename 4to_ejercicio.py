'''
Escribir una funcion que reciba una cadena
y devuelva una diccionario con la cntidad
de apariciones de cda palabra en la cadena. Por
ejmplo, si recibe "Que lindo dia que hace
hoy" debe volver:
'que':2, 'lindo':1, 'dia':1, 'hace':1, 'hoy':1
'''
oracion='Que lindo dia que hace hoy'
def recibir(oracion):
    a=oracion.lower()
    print(a)
    b=a
    sub='que'
    sub1='lindo'
    sub2='dia'
    sub3='hace'
    sub4='hoy'
    t=a.count(sub)
    d=a.count(sub1)
    d=a.count(sub2)
    d=a.count(sub3)
    d=a.count(sub4)
    print(t)
    diccion={

    }
    if 'que'in a:
        diccion.update({'que':t})
    else:
        print('no esta')
    if 'lindo'in a:
        diccion.update({'lindo':d})
    else:
        print('no esta')
    if 'dia'in a:
        diccion.update({'dia':d})
    else:
        print('no esta')  
    if 'hace'in a:
        diccion.update({'hace':d})
    else:
        print('no esta') 
    if 'hoy'in a:
        diccion.update({'hoy':d})
    else:
        print('no esta') 
    print(diccion)
    
print(recibir(oracion))        
