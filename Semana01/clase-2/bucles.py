# for - while

cursos =  [
    "Javascript",
    "Python",
    "HTML",
    "CSS",
]

alumnos = [
    {"id": 1, "name": "Juan"},
    {"id": 2, "name": "Ana"},
    {"id": 3, "name": "Luis"},
    {"id": 4, "name": "Maria"},
]

print(f"Curso: {len(alumnos)}")

for curso in cursos:
    print(f"Curso: {curso}")

for alumno in alumnos:
    print(alumno.get("name"))

persona = {
    "nombre" : "Juan",
    "apellido" : "Perez",
    "direccion" : "Calle Falsa 123",
}

# for key in persona:
print("=" * 20)
for p in persona:
    print(p)

##El primer for (for i in persona.items()) es útil cuando necesitas trabajar con el par clave-valor como una tupla, por ejemplo,
# para almacenarlo en una lista o pasarlo a una función que espera tuplas.
print("=" * 20)
for i in persona.items():
    print(i)

#El segundo for (for key, value in persona.items()) es útil cuando quieres manipular o mostrar la clave y el valor por separado,
# como al formatear la salida o aplicar lógica diferente según la clave o el valor.
print("=" * 20)
for key, value in persona.items():
    print(f"{key}: {value}")

# El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera.
while True:
    respuesta = input("¿Deseas continuar? (s/n): ")
    if respuesta.lower() == 'n':
        print("Saliendo del bucle.")
        break
    elif respuesta.lower() == 's':
        print("Continuando...")
    else:
        print("Respuesta no válida, por favor ingresa 's' o 'n'.")
    dato = input("Ingresa tu nombre: ")
    print(dato)
    if dato == "salir":
        break # termina la ejecución del bucle


