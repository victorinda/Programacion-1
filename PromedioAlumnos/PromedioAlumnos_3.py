from sys import stderr

# Capturar la cantidad de alumnos.
while True:
    try:
        n = int(input("¿A cuantos alumnos se les va a capturar calificación? "))
        if n >= 1:
            break
        print("Se debe capturar al menos una calificacion")
    except ValueError:
        print("Error: El valor debe ser un entero", file=stderr)
        
        
alumnos = []
suma = 0
# Capturar el nombre y calificación de cada alumno.
for i in range(1, n+1):
    # Validar el nombre.
    while True:
        nombre = input(f"Nombre del alumno {i}: ")
        if nombre != "":
            break
        print("El nombre no puede estar vacio")
    # Validar la calificación.
    while True:
        try:
            calif = int(input(f"Calificacion del alumno {i}: "))
            if 0 <= calif <= 100:
                break
            print("La calificación debe estar en [0, 100]")
        except ValueError:
            print("Error: El valor debe ser un entero", file=stderr)
    # Agregar la pareja nombre, califcacion a la lista de alumnos.
    alumnos.append([nombre, calif])
    # Añadir la calificación a la sumatoria.
    suma += calif
    
# Calcular el promedio grupal.
promedio = suma/n

# Obtener la lista de alumnos con calificacion mayor al promedio.
alumnos_supprom = [alumno for alumno in alumnos if alumno[1] > promedio]

# Imprimir el promedio grupal.
print(f"\nPromedio grupal:\n{promedio}")

# Imprimir los alumnos con calificacion mayor al promedio.
print("\nCalificaciones superiores al promedio: ")
for alumno in alumnos_supprom:
    print(f"{alumno[0]}: {alumno[1]}")
