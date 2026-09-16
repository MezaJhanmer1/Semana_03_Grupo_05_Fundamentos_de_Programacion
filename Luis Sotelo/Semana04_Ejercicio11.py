#definir var dentro de una funcion con valor inicial false

def crear_interruptor():
    estado = False          #variable tiene un valor False

    def cambiar():
        nonlocal estado         #permite modificar la variable sin crear otra nueva
        estado = not estado     # cambia el valor de False a True
        return "ON" if estado else "OFF"    #retorna ON si el valor es TRUE y OFF si el valor es FALSE
    return cambiar              #me retorna el flujo, no el resultado

switch = crear_interruptor()    #la variable switch es llamada. el estado inicial ya quedó guardado y congelado en False

print(switch()) # ON        #por estar en False cambia a True 
print(switch()) # OFF       #por estar en True cambia a False 
print(switch()) # ON        #por estar en False cambia a True 