

def calcular_salario_mensual(horas_trabajadas, precio_por_hora):
    semanas_por_mes = 4.2
    salario_semanal = horas_trabajadas * precio_por_hora
    salario_mensual = salario_semanal * semanas_por_mes
    deduccion_cargas_sociales = salario_mensual * 0.105  # 10.5% de deducción por cargas sociales
    deduccion_asociacion_solidarista = salario_mensual * 0.05  # 5% de deducción por asociación solidarista
    salario_mensual_despues_deducciones = salario_mensual - deduccion_cargas_sociales - deduccion_asociacion_solidarista
    return salario_mensual_despues_deducciones

horas_trabajadas = int(input("Ingrese la cantidad de horas semanales trabajadas: "))
precio_por_hora = float(input("Ingrese el precio por hora: "))

salario_mensual = calcular_salario_mensual(horas_trabajadas, precio_por_hora)

print("El salario mensual después de las deducciones es: $", salario_mensual)