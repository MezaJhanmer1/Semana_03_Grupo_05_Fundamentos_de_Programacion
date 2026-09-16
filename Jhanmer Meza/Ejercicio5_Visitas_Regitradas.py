visitas = 0 # global
def registrar_visita():
    # Indicamos que vamos a utilizar la variable global "visitas"
    global visitas
    visitas += 1
     # Mostramos el número de visita registrada
    print(f"Visita #{visitas} registrada")
# Llamamos a la función: visitas pasa de 0 a 1    
registrar_visita() # Visita #1
# Volvemos a llamar a la función: visitas pasa de 1 a 2
registrar_visita() # Visita #2
# Mostramos el valor final de la variable global
print(f"Total: {visitas}") # Total: 2
