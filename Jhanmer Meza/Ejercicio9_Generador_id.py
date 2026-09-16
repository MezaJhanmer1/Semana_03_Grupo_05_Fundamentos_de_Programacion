def generador_id():
    ultimo_id = 0

    def nuevo_id():
        # Le decimos a Python que "ultimo_id" pertenece a la función exterior (generador_id).
        #No es una variable global, es una variable de la funcion de fuera
        nonlocal ultimo_id

        # Aumentamos el ID en 1.
        ultimo_id += 1

        # mostrar el número con 4 dígitos, rellenando con ceros a la izquierda".
        return f"ID-{ultimo_id:04d}"
    # Retornamos la función nuevo_id
    return nuevo_id

gen = generador_id()
print(gen()) # ID-0001
print(gen()) # ID-0002