MODO_DEBUG = True  # global (constante)

def procesar(dato):                    # define la función
    if MODO_DEBUG:                     # lee la global; sin 'global' porque no reasigna
        print(f"[DEBUG] Procesando: {dato}")
    return dato.upper()                # siempre devuelve en MAYÚSCULAS

print(procesar("hola"))                # imprime el retorno → "HOLA"