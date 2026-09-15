#Contar Vocales con Variables locales

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    conteo = 0 # local

    for letra in texto:
     if letra in vocales:
        conteo += 1
    return conteo
print(contar_vocales("Hola Mundo")) # 4

#Agregado
def contar_ñ(texto):
    consonante = "ñ"
    conteo = 0 # local

    for letra in texto:
     if letra in consonante:
        conteo += 1
    return conteo

print(contar_ñ("Hola ñandú")) # 4