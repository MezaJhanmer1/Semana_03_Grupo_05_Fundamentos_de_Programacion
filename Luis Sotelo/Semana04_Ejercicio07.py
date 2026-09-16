
inventario = [] # global

def agregar(producto):
    global inventario
    inventario.append(producto) #agregar un elemento al final de la lista

def mostrar():
    for p in inventario:   #para la variable p dentro de la lista inventario
        print(f" -{p}")

        
agregar("Laptop")
agregar("Mouse")
mostrar()
# -Laptop