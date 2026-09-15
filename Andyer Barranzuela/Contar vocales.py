def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    conteo = 0  # Variable local
    for letra in texto:
        if letra in vocales:
            conteo += 1
    return conteo

print(contar_vocales("Hola Mundo"))  # Imprime: 4