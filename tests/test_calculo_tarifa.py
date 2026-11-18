def test_calculo_tarifa():
    # Definir los datos de entrada
    distancia = 10
    tarifa_por_km = 2

    # Ejecutar el calculo
    tarifa_total = distancia * tarifa_por_km

    # Verificar el resultado
    assert tarifa_total == 20

def test_calculo_tarifa_larga():
    # Definir los datos de entrada
    distancia = 15
    tarifa_por_km = 3

    # Ejecutar el calculo
    tarifa_total = distancia * tarifa_por_km

    # Verificar el resultado
    assert tarifa_total == 45