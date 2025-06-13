# Funciones
def saludar():
    print("Hola, ¿cómo estás?")

def saludar_persona(nombre):
    print(f"Hola, {nombre}, ¿cómo estás?")

saludar()
saludar_persona("Juan")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calcular(operation, a, b):
    if operation == "sumar":
        return print(sumar(a, b),"es el resultado de la suma")
    elif operation == "restar":
        return print(restar(a, b),"es el resultado de) la resta")
    elif operation == "multiplicar":
        return print(multiplicar(a, b),"es el resultado de la multiplicación")
    elif operation == "dividir":
        return print(dividir(a, b),"es el resultado de la división")
    else:
        return "Operación no válida"

calcular('sumar', 5, 3)
calcular("restar", 10, 4)
calcular("multiplicar", 2, 6)
calcular("dividir", 8, 2)
calcular("dividir", 8, 0)  # Manejo de división por cero

# Funciones con parámetros por defecto
def saludar_con_prefijo(nombre, ):
    print(f"tu nombre es {nombre}")

#saludar_con_prefijo(input("Ingrese nombre: "))

def dividir(n1, n2) -> float:
    return n1 / n2

print(dividir(10, 2))  # Imprime 5.0

def sumatoria(*args):
    return sum(args)

print(sumatoria(1, 2, 3, 4, 5))  # Imprime 15

# Funciones anónimas (lambdas)
duplicar = lambda n: n * 2
print("duplicar: ",duplicar(5))  # Imprime 10
