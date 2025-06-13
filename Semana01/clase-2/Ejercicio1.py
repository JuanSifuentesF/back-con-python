# Enunciado: Crear un sistema que permita:
# 1. Ingresar nombre, edad y lista de compras (3 productos con precio).
# 2. Calcular el total de la compra con IGV
# 3. Imprimir resumen de datos del usuario, lista de productos,
# total y si tiene descuento (si el total > 500)

def ingresar_datos():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))

    productos = []
    for i in range(3):
        producto = input(f"Ingrese el nombre del producto {i+1}: ")
        precio = float(input(f"Ingrese el precio del producto {i+1}: "))
        productos.append({"nombre": producto, "precio": precio})

    return nombre, edad, productos

def calcular_total(productos):
    total = sum(producto["precio"] for producto in productos)
    igv = total * 0.18
    total_con_igv = total + igv
    return total_con_igv

def tiene_descuento(total):
    return total > 500

def imprimir_resumen(nombre, edad, productos, total):
    print("\nResumen de Datos:")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print("Lista de Productos:")
    for producto in productos:
        print(f"- {producto['nombre']}: S/{producto['precio']:.2f}")
    print(f"Total de la compra con IGV: S/{total:.2f}")

    if tiene_descuento(total):
        print("¡Tiene descuento!")
    else:
        print("No tiene descuento.")

def main():
    nombre, edad, productos = ingresar_datos()
    total = calcular_total(productos)
    imprimir_resumen(nombre, edad, productos, total)

main()
