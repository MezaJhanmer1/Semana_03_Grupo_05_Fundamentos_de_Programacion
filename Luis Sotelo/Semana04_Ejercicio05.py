#Definir visitas con variables globales

visitas = 2 # global
def registrar_visita():
    global visitas #usar la variable global y no crear una local
    visitas += 1 #cada vez q se ejecuta la funcion suma uno.
    print(f"Visita #{visitas} registrada")  #llamar variables dentro de llaves

registrar_visita() # Visita #1
registrar_visita() # Visita #2
registrar_visita() # Visita #3

print(f"Total: {visitas}") # Total: 5