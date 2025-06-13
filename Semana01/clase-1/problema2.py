# Calcular si la edad ingresada por el usuario es mayor o menor de edad
edad = int(input("Ingrese la edad: "))

"""
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
"""

# para estos casos existe el operador ternario
resultado = "Mayor de edad" if edad >= 19 else "Menor de edad"
print(resultado)
