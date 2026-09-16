MODO_DEBUG = True # global (constante)

def procesar(dato):
    # Comprobamos el valor de la variable global MODO_DEBUG
    if MODO_DEBUG: # lectura sin 'global'
        
        print(f"[DEBUG] Procesando: {dato}")
    # Convertimos el dato a mayúsculas y lo devolvemos
    return dato.upper()
procesar("hola") # [DEBUG] Procesando: hola