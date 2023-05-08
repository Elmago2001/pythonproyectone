alumnos = {}

def obtener_calificaciones(materia):
    """Obtiene las calificaciones de una materia."""
    califs = []
    for i in range(3):
        calif = float(input("Ingrese la calificacion de {} del parcial {}: ".format(materia,i+1)))
        califs.append(calif)
    return califs

materias_nombres = dict()
while True:

    nombre = input("Ingrese una de las acciones ('A' para agregar las materias, 'C' para capturar la informacion o 'S' para terminar): ")
    if nombre == "S":
        break
    elif nombre == "A":
        materias= int(input("Cantidad de materias: "))
        for e in range (materias):
           name = input("Dame el nombre de la materia: ")
           materias_nombres[name] = ''
           
    elif nombre == "C":
        nombre = input("Dame el nombre del alumno: ")
        email = input("Ingrese el correo electronico del alumno: ")
        if len(dict.keys(materias_nombres)) > 0:
            calificaciones ={i: obtener_calificaciones(i) for i in materias_nombres}
            
        alumnos[nombre] = {"email": email, "calificaciones": calificaciones}


def calcular_promedio(calificaciones):
    """Calcula el promedio de una lista de calificaciones."""
    return sum(calificaciones) / len(calificaciones)

for nombre, info in alumnos.items():
    calificaciones = info["calificaciones"]
    promedios = { materia: calcular_promedio(califs) for materia, califs in calificaciones.items() }
    promedio_general = sum(promedios.values()) / len(promedios)
    print(f"Nombre: {nombre}")
    print(f"Correo electronico: {info['email']}")
    print(f"Promedio general: {promedio_general:.2f}\n")
