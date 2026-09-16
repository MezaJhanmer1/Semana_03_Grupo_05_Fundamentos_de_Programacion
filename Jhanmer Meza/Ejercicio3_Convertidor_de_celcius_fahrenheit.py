# "c" es el parámetro que recibirá la temperatura en Celsius
def celsius_a_fahrenheit(c):
     # Calculamos el factor de conversión, 9/5 = 1.8
    factor = 9 / 5 # local
    # Aplicamos la fórmula para convertir Celsius a Fahrenheit
    # Fahrenheit = Celsius × 1.8 + 32
    fahrenheit = c * factor + 32 # local
    # Devolvemos el resultado de la conversión
    return fahrenheit
# Llamamos a la función enviando 100 grados Celsiu
print(celsius_a_fahrenheit(100)) # 212.0
#llamamos nuevamente a la función, pero ahora enviamos 0 grados Celsius
print(celsius_a_fahrenheit(0)) # 32.0
