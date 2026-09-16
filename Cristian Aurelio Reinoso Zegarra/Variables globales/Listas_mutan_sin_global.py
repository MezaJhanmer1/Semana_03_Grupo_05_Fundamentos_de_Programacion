# Las listas/dicts se MUTAN sin 'global'
# (porque no se reasigna la referencia)

notas = []                  # GLOBAL: lista compartida

def agregar_nota(n):        # define la función con parámetro 'n'
    notas.append(n)         # sin 'global': solo MUTA la lista

agregar_nota(95)            # notas = [95]
print(notas)                # [95]