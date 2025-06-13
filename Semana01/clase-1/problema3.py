# Averiguar si el número ingresado por el usuario es par o impar

numero = int(input("Ingrese un numero: "))

resultado = f"El {numero} es par " if numero % 2 == 0 else f"El {numero} es impar "
print(resultado)
"""
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")
"""
