'''6. Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las
facturas se almacenaran en un diccionario donde la clave de cada factura sera el numero de
factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere anadir
una nueva factura, pagar una existente o terminar. Si desea anadir una nueva factura se
preguntara por el numero de factura y su coste y se anadira al diccionario. Si se desea pagar
una factura se preguntara por el numero de factura y se eliminara del diccionario. Despues de
cada operacion el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y
la cantidad pendiente de cobro.'''

facturas_pendientes = {}

while True:
    opcion = input("Introduzca 'A' para anadir una factura, 'P' para pagar una existente o 'T' para terminar: ")
    
    if opcion.upper() == 'A':
        numero_factura = input("Introduzca el numero de factura: ")
        coste_factura = float(input("Introduzca el coste de la factura: "))
        facturas_pendientes[numero_factura] = coste_factura
        
        cantidad_cobrada = sum(facturas_pendientes.values())
        cantidad_pendiente = 0 if cantidad_cobrada == 0 else sum(facturas_pendientes.values()) - min(facturas_pendientes.values())
        print(f"Cantidad cobrada hasta el momento: {cantidad_pendiente:.2f}")
        print(f"Cantidad pendiente de cobro: {cantidad_cobrada:.2f}")
    
    elif opcion.upper() == 'P':
        numero_factura = input("Introduzca el numero de factura a pagar: ")
        if numero_factura in facturas_pendientes:
            factura_pendiente = facturas_pendientes[numero_factura]
            cantidad_a_pagar = float(input(f"Ingrese la cantidad a pagar (deuda pendiente {factura_pendiente:.2f}): "))
            if cantidad_a_pagar >= factura_pendiente:
                sobrante = cantidad_a_pagar - factura_pendiente
                del facturas_pendientes[numero_factura]
                if sobrante > 0:
                    print(f"Se ha pagado la factura {numero_factura} con un coste de {factura_pendiente:.2f}. Sobran {sobrante:.2f}")
                else:
                    print(f"Se ha pagado la factura {numero_factura} con un coste de {factura_pendiente:.2f}")
            else:
                facturas_pendientes[numero_factura] = factura_pendiente - cantidad_a_pagar
                print(f"Se ha pagado parcialmente la factura {numero_factura}, quedando una deuda pendiente de {facturas_pendientes[numero_factura]:.2f}")
        else:
            print("No se ha encontrado la factura especificada.")
        
        cantidad_cobrada = sum(facturas_pendientes.values())
        cantidad_pendiente = 0 if cantidad_cobrada == 0 else sum(facturas_pendientes.values()) - min(facturas_pendientes.values())
    
    elif opcion.upper() == 'T':
        break
    
    else:
        print("Opcion no valida.")