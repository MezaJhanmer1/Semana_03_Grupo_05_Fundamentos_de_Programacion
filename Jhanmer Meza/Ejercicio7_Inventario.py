# Creamos una lista llamada inventario
inventario = [] # global

# Función para agregar un producto al inventario
def agregar(producto):
     # Indicamos que vamos a trabajar con la variable global
    global inventario

     # .append() agrega el producto al final de la lista.
    inventario.append(producto)

# Función para mostrar todos los productos del inventario
def mostrar():

    # Recorremos cada elemento de la lista "inventario"y en cada vuelta, "p" representa un producto
    for p in inventario:
         # Mostramos el producto en pantalla.
        print(f" - {p}")

# Llamamos a la función agregar() y le enviamos "Laptop".
agregar("Laptop")
agregar("Mouse")

# Llamamos a mostrar() para recorrer e imprimir
mostrar()
# - Laptop