"""
- Variables, Sintaxis, Tipos de Datos
strings: str
numeros enteros: int
numeros decimales: float
boleans: bool
null: None

Lenguaje fuertemente tipado como no
"""

altura = None # null
curso = "Backend" # string -> str
edad = 30 # int
altura = 1.8

# usamos _ (snake_case)
es_estudiante = True
es_mayor = False
nombre_completo = "Juan Sifuentes"

print(altura)
print(curso)
print(es_estudiante)

"""
- Aritméticos => +, -, *, /, **, //, %
- Comparación => ==, !=, >, <, >=, <=
- Lógicos => and, or, not, is
"""

n1 = 10
n2 = 5

print("Suma: ",n1 + n2)
print("Resta: ",n1 - n2)
print("Multiplicación: ",n1 * n2)
print("División: ",n1 / n2)
print("Residuo: ",n1 % n2)
print("Potencia: ",n1 ** n2)
print("División entera: ",n1 // n2)

print("==================")


# f string
print(f"Igualdad: {n1 == n2}")
print(f"Desigualdad: {n1 != n2}")
print(f"Mayor: {n1 > n2}")
print(f"Menor: {n1 < n2}")
print(f"Mayor o igual: {n1 >= n2}")

print("=================")
print(n1 == 10 and n2 == 5)
print(n1 > 10 or n2 <= 5)

print("=================")
if n1 == 10 and n2 <= 5:
    print("Se encontró alguna incidencia")
else:
    print("NO hay coincidencias")



