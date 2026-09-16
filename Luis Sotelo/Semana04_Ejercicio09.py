#var nonlocal desde otra funcion

def generador_id():
    ultimo_id = 0  # no es una var global

    def nuevo_id():         #generamos una subfuncion para imprimir los ID
        nonlocal ultimo_id  #permite modificar la variable sin crear otra nueva
        ultimo_id += 1      # sumar 1 cada vez que encuentre la variable
        return f"ID-{ultimo_id:04d}"  #retorna el print y el :04d muestra 4 numeros precisos
    return nuevo_id        # función que sume y devuelva el ID, pero que no resetee el contador cada vez q se usa.

gen = generador_id()        #gen q es igual al retorno del return id, y todo en vivo, esto permite guardar el valor.
print(gen()) # ID-0001
print(gen()) # ID-0002