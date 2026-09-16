inventario = []                  # GLOBAL

def agregar(producto):           # define función con parámetro 'producto'
    global inventario            # NO hace falta: append() muta, no reasigna
    inventario.append(producto)  # añade al final de la lista global

def mostrar():                   # define función sin parámetros
    for p in inventario:         # recorre la global (solo lee → sin 'global')
        print(f" - {p}")         # imprime cada producto

agregar("Laptop")                
agregar("Mouse")                 
mostrar()                        # imprime los dos