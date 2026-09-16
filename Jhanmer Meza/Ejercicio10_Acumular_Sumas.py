def crear_acumulador():
    total = 0
    # Indicamos que queremos modificar la variable "total" que pertenece a la función exterior.
    def acumular(valor):
        nonlocal total
        # Sumamos el valor recibido a total
        total += valor
        # Devolvemos el total acumulado.
        return total
    # Devolvemos la función "acumular".
    return acumular
# "suma" recibe la función acumular.
suma = crear_acumulador()
print(suma(10)) # 10
print(suma(5)) # 15
