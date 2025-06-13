# arreglo => lista
alumnos = [
    "Juan",
    "Irving",
    "Nicolas",
    "Lucas",
    "Mario"
]

print(type(alumnos))
print(alumnos[3])

# Agregar un valor
print("*"*10 , 'Agregar', "*"*10)
alumnos.append("Maria")
print(alumnos)

# eliminar un valor
print("*"*10 , 'Remove', "*"*10)
alumnos.remove("Lucas")

# insert
print("*"*10 , 'Insert', "*"*10)
alumnos.insert(3, "Marcos")
print(alumnos)

# ordenar
print("*"*10 , 'Ordenar', "*"*10)
print(sorted(alumnos))

# ordenar al revés
print("*"*10 , 'Ordenar al revés', "*"*10)
print(
    sorted(alumnos, reverse=True)
)

# index
print("*"*10 , 'Index', "*"*10)
print(alumnos.index("Juan"))
print(alumnos.index("Marcos"))