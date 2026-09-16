# "numeros" será la lista que recibiremos
def promedio(numeros):
    # sum() suma todos los números de la lista
    # "total" es una variable LOCAL porque existe dentro de la función
    total = sum(numeros) # local
    # len() cuenta cuántos elementos hay en la lista
    n = len(numeros) # local
    # Esto evita intentar dividir entre cero
    return total / n if n else 0
# Llamamos a la función enviándole una lista de números
print(promedio([10, 20, 30])) # 20.0