def celsius_a_fahrenheit(c):
    factor = 9 / 5  # local
    fahrenheit = c * factor + 32  # local
    return fahrenheit

print(celsius_a_fahrenheit(100))  # Imprime: 212.0
print(celsius_a_fahrenheit(0))    # Imprime: 32.0