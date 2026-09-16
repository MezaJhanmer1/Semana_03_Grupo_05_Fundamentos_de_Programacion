

# Las listas/dicts se MUTAN sin 'global'
# (porque no se reasigna la referencia)
notas = []
def agregar_nota(n):
    notas.append(n) # ← sin 'global' #no necesita global cuando modificamos el interior con estas herramientas
                    # toma lo que ha llegado a n y lo pone al final de la lista

agregar_nota(95)
agregar_nota(80)

print(notas) # [95]