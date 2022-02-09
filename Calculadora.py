def suma(x,y):
    return x + y


while True:
    operador1 = int(input("Introduzca el primer operador: "))
    operador2 = int(input("Introduzca el segundo operador: "))
    operacion = input(("""
    Seleccione la operación que desee realizar:
    (S) Suma
    (R) Resta
    (M) Multiplica
    (D) Dividir
    (P) Potencia
    (E) Exit
    """))
    match operacion:
        case "S":
            suma (operador1, operador2)
