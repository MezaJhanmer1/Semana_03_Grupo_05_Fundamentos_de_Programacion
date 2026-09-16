def crear_interruptor():                 # función externa
    estado = False                       # se recuerda entre llamadas
    def cambiar():                       # función interna
        nonlocal estado                  # sin esto, crearía una local nueva
        estado = not estado              # invierte True ↔ False
        return "ON" if estado else "OFF"
    return cambiar                       # devuelve la función interna

switch = crear_interruptor()
print(switch())                          # ON
print(switch())                          # OFF
print(switch())                          # ON