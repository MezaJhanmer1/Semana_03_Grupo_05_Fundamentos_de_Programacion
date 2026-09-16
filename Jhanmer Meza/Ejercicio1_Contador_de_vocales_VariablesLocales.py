# Creamos una función llamada contar_vocales, con el parametro texto
def contar_vocales(texto):
    # Guardamos todas las vocales que queremos reconocer
    vocales = "aeiouAEIOU"
    # Esta variable es LOCAL: solo existe dentro de la función, nos ayuda para contar las vocales comienza en 0
    conteo = 0 # local
    # Recorremos letra por letra el texto que recibimos
    for letra in texto:
        # Preguntamos si la letra actual está dentro de "vocales"
        if letra in vocales:
            #Si encontramos una vocal, aumentamos el contador en 1
            conteo += 1
    # Cuando termina el for, devolvemos la cantidad de vocales encontradas
    return conteo
# Cuando termina el for, devolvemos la cantidad de vocales encontradas, con print nos muestra el resultado en pantalla
print(contar_vocales("Hola Mundo")) # 4