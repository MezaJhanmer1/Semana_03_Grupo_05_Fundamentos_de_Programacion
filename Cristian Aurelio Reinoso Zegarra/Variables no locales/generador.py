def generador_id():              # función externa 
    ultimo_id = 0                # variable del ámbito envolvente

    def nuevo_id():              # función interna
        nonlocal ultimo_id       # sin esto, crearía una local nueva
        ultimo_id += 1           # modifica la variable de generador_id
        return f"ID-{ultimo_id:04d}"   # formato 4 dígitos con ceros

    return nuevo_id              # devuelve la función interna (no la ejecuta)

gen = generador_id()             # gen guarda 'nuevo_id' con su propio ultimo_id
print(gen())                     # ID-0001
print(gen())                     # ID-0002