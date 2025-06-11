# dict => obj
persona = {
    "nombre": "Juan",
    "edad": 30,
    1: "Numero",
    "profesión": "Desarrollador"
}
print(type(persona))
print(persona)

print(persona.get("dirección", "No existe la clave"))
print("=" * 10, "UPDATE", "=" * 10)
persona.update({"dirección": "Lima"})
print(persona)
persona.pop(1)
print(persona)
