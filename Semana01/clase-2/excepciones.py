try:
    print(10/0)  # Esto generará un error de división por cero
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

try:
    letras = ["a", "b", "c"]
    print(letras[5])  # Esto generará un error de índice fuera de rango
except IndexError:
    print("Error: Índice fuera de rango. Asegúrate de que el índice esté dentro del rango de la lista.")


def dividir():
    try:
        numero1 = int(input("Ingrese el primer número: "))
        numero2 = int(input("Ingrese el segundo número: "))
        print(numero1 / numero2)
    except ZeroDivisionError:
        print("No es posible dividir por cero.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("Operación de división finalizada.")

    print("="*20, "IndexError", "="*20)

    try:
        letras = ["a", "b", "c"]
        print(letras[10])
    except IndexError:
        print("Error: Índice fuera de rango. Asegúrate de que el índice esté dentro del rango de la lista.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        print("Operación de acceso a lista finalizada.")
        print("Operación de división finalizada.")

try:
    persona = {"id": 1, "name": "Juan"}
    persona["last_name"]  # Intento de acceder a una clave que no existe
except KeyError:
    print("Error: La clave 'last_name' no existe en el diccionario 'persona'. Asegúrate de que la clave esté presente antes de acceder a ella.")

try:
    print("2"+ 2) # Intento de concatenar un string con un entero
except TypeError as e:
    print(f"Error: {e}. No se puede concatenar una cadena y un número. Asegúrate de convertir el número a cadena antes de concatenar.")