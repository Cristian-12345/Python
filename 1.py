dia_semana = input("Ingrese el dia: ")
t_estacionado = float(input("Ingrese el tiempo en horas: "))

cobro = {
    "lunes": 2.00,
    "martes": 2.00,
    "miercoles": 2.00,
    "jueves": 2.50,
    "viernes": 2.50,
    "sabado": 3.00,
    "domingo": 3.00
}

if dia_semana in cobro:
    if t_estacionado > 0:
        total = 0.0

        horas = int(t_estacionado)
        minutos_fraccion = t_estacionado - horas

        if minutos_fraccion >= 0.5:
            horas += 1

        total = cobro[dia_semana] * horas

        print("El dinero que tiene que pagar es: $", total)
    else:
        print("Tiempo ingresado incorrecto, debe ingresar un tiempo mayor a 0.")
else:
    print("Dia de la semana incorrecto.")