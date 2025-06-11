"""
Pedir al usuario 3 notas y evaluar el promedio de estos,
en caso la nota sea mayor a 16, imprimir sobresaliente,
caso contrario imprimir en trabajo
"""

nota1 = float(input("Ingrese nota1: "))
nota2 = float(input("Ingrese nota2: "))
nota3 = float(input("Ingrese nota3: "))

resultado = "Sobresaliente" if (nota1 + nota2 + nota3) / 3 > 16 else "En trabajo"

print(resultado)