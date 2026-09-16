# Las listas/dicts se MUTAN sin 'global'
# (porque no se reasigna la referencia)
notas = []

def agregar_nota(n):
     # .append() AGREGA un elemento a la lista existente.
    # No estamos creando una nueva lista ni cambiando la referencia de "notas", simplemente modificamos su contenido.
    # Por eso NO necesitamos escribir "global notas".
    notas.append(n) # ← sin 'global'
agregar_nota(95)
print(notas) # [95]