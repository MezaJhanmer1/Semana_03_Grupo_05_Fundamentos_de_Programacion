def crear_acumulador():          # función externa
    total = 0                    # variable del ámbito envolvente

    def acumular(valor):         # función interna
        nonlocal total           # sin esto, crearía una local nueva
        total += valor           # modifica 'total' de crear_acumulador
        return total             # devuelve el acumulado actual

    return acumular              # devuelve la función interna

suma = crear_acumulador()        # suma guarda 'acumular' con su propio 'total'
print(suma(10))                  # 10
print(suma(5))                   # 15