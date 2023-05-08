tabla_periodica = (
    {'alias': 'HIDROGENO', 'nombre': 'Hidrógeno', 'numero_atomico': 1, 
    'masa_atomica': 1.008, 'simbolo_quimico': 'H', 
    'configuracion_electronica': '1s1'},    
    {'alias': 'HELIO', 'nombre': 'Helio', 'numero_atomico': 2,
    'masa_atomica': 4.003, 'simbolo_quimico': 
    'He', 'configuracion_electronica': '1s2'},
    {'alias': 'LITIO', 'nombre': 'Litio', 'numero_atomico': 3, 
    'masa_atomica': 6.941, 'simbolo_quimico':
    'Li', 'configuracion_electronica': '[He] 2s1'},    
    {'alias': 'BERILIO', 'nombre': 'Berilio', 'numero_atomico': 4, 
    'masa_atomica': 9.012, 'simbolo_quimico': 'Be',
    'configuracion_electronica': '[He] 2s2'},
    {'alias':'BORO','nombre': 'Boro', 'numero_atomico': 5, 
    'masa_atomica': 10.81, 'simbolo_quimico': 'B',
    'configuracion_electronica': '[He] 2s2 2p1'},
    {'alias':'CARBONO', 'nombre': 'Carbono', 'numero_atomico': 6,
    'masa_atomica': 12.01, 'simbolo_quimico': 'C',
    'configuracion_electronica': '[He] 2s2 2p2'},
    {'alias':'NITROGENO', 'nombre': 'Nitrógeno', 'numero_atomico': 7,
    'masa_atomica': 14.01, 'simbolo_quimico': 'N', 
    'configuracion_electronica': '[He] 2s2 2p3'},
    {'alias':'OXIGENO', 'nombre': 'Oxígeno', 'numero_atomico': 8, 
    'masa_atomica': 16.00, 'simbolo_quimico': 'O',
    'configuracion_electronica': '[He] 2s2 2p4'},
    {'alias':'FLUOR', 'nombre': 'Flúor', 'numero_atomico': 9, 
    'masa_atomica': 19.00, 'simbolo_quimico': 'F',
    'configuracion_electronica': '[He] 2s2 2p5'},
    {'alias':'NEON', 'nombre': 'Neón', 'numero_atomico': 10,
    'masa_atomica': 20.18, 'simbolo_quimico': 'Ne',
    'configuracion_electronica': '[He] 2s2 2p6'},
    {'alias':'SODIO', 'nombre': 'Sodio', 'numero_atomico': 11,
    'masa_atomica': 22.99, 'simbolo_quimico': 'Na',
    'configuracion_electronica': '[Ne] 3s1'},
    {'alias':'MAGNESIO', 'nombre': 'Magnesio', 'numero_atomico': 12,
    'masa_atomica': 24.31, 'simbolo_quimico': 'Mg',
    'configuracion_electronica': '[Ne] 3s2'},
)

nombre_var = input('Dame el nombre del elemento: ').upper()

nombresElementos = [i["alias"] for i in tabla_periodica]
indexes = [i for i, x in enumerate(nombresElementos) if x == nombre_var]

if len(indexes) > 0:
    print(tabla_periodica[indexes[0]])
else:
    print("El elemento no se encuentra en los primeros 12 elementos de la tabla periodica.")
