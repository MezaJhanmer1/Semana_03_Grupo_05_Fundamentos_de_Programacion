

def crear_acumulador():
    total = 0

    def acumular(valor):
        nonlocal total
        total += valor
        return total
    return acumular         #función que sume y devuelve el total , pero que no resetee el contador cada vez q se usa.

suma = crear_acumulador()   #suma q es igual al retorno de acumular, y todo en vivo, esto permite guardar el valor.
print(suma(10)) # 10
print(suma(5)) # 15
#agregado
print(suma(10)) # 15