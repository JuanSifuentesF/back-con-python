# Tema: Librerias y Módulos
# Las librerías y módulos son colecciones de código reutilizable que puedes importar en tus programas para evitar duplicar código y facilitar el mantenimiento.

import math
import random
import datetime

print("Módulo math:", math.pi)  # Imprime el valor de pi
print("Redondeo de 3.2:", math.floor(3.2))  # Imprime el valor de 3.2 redondeados hacia abajo
print("Redondeo de 3.7:", math.ceil(3.7))  # Imprime el valor de 3.7 redondeados hacia arriba
print("Raíz cuadrada de 16:", math.sqrt(16))  # Imprime la raíz cuadrada de 16
print("Logaritmo natural de 10:", math.log(10))  # Imprime el logaritmo natural de 10
print("Factorial de 5:", math.factorial(5))  # Imprime el factorial de 5
print("Valor absoluto de -5:", abs(-5))  # Imprime el valor absoluto de -5
print("Seno de 30 grados:", math.sin(math.radians(30)))  # Imprime el seno de 30 grados
print("Coseno de 60 grados:", math.cos(math.radians(60)))  # Imprime el coseno de 60 grados
print("Tangente de 45 grados:", math.tan(math.radians(45)))  # Imprime la tangente de 45 grados
print("Exponencial de 2:", math.exp(2))  # Imprime el valor que se ha elevado a la potencia de 2
print("Logaritmo en base 10 de 100:", math.log10(100))  # Imprime el logaritmo en base 10 de 100
print("Logaritmo en base 2 de 8:", math.log2(8))  # Imprime el logaritmo en base 2 de 8
print("Combinaciones de 5 elementos tomados de 2 en 2:", math.comb(5, 2))  # Imprime el número de combinaciones

print("     " * 20)

print("Random <<<<<<<<<<<<<<<<<<<<<")
print(random.randint(1, 10))  # Imprime un número aleatorio entre 1 y 10
print(random.uniform(1, 10))  # Imprime un número aleatorio entre 1.0 y 10.0

participantes = ["Juan", "Ana", "Luis", "Maria"]

print(random.choice(participantes))  # Imprime un participante aleatorio de la lista
print(random.sample(participantes, 2))  # Imprime una muestra aleatoria de 2 participantes de la lista
print(random.shuffle(participantes))  # Mezcla la lista de participantes en su lugar
print(participantes)  # Imprime la lista de participantes mezclada

print("     " * 20)

print("Datetime <<<<<<<<<<<<<<<<<<")
print(datetime.datetime.now())
hoy = datetime.date.today()
print(hoy.strftime("%a/%m/%Y"))







