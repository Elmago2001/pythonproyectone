'''8. El directorio de los clientes de una empresa está organizado en una cadena de texto como la de
más abajo, donde cada línea contiene la información del nombre, email, teléfono, nif, y el

descuento que se le aplica.
Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los
nombres de los campos con la información contenida en el directorio.

directorio="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzal
ez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;
8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sán
chez;carmen@mail.com;667677855;15.7"
Escribir un programa que convierta esa cadena en una lista de diccionarios con los campos
correspondientes

{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfo
no': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', '
email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M
': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888
233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen
@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}'''

directorio="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

lineas = directorio.split("\n")
nombres_campo = lineas[0].split(";")
clientes = []
for i in range(1, len(lineas)-1):
    campos = lineas[i].split(";")
    cliente = {}
    for j in range(len(campos)):
        cliente[nombres_campo[j]] = campos[j]
    clientes.append(cliente)

clientes_dict = {}
for cliente in clientes:
    nif = cliente["nif"]
    del cliente["nif"]
    clientes_dict[nif] = cliente

print(clientes_dict)