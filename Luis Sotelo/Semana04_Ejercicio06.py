

MODO_DEBUG = True # global (constante) la variable tiene condicion de verdadero para que funcione dentro de la funcion.
def procesar(dato):
    if MODO_DEBUG: # lectura sin 'global' si la variable es verdadera
        print(f"[DEBUG] Procesando: {dato}")
    return dato.upper() # lo lanza hacia afuera de la función pero como no hay print no lo muestra y se pierde.


procesar("hola") # [DEBUG] Procesando: hola 

print(procesar("hola")) #Al haber print  retorna el dato en mayuscula y la frase completa de arriba.
