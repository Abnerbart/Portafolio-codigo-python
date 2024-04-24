def costo_traslado(distancia, costo_por_km, dias_por_semana, semanas_cuatrimestre):
    distancia_semanal = distancia * 2 * dias_por_semana
    distancia_total = distancia_semanal * semanas_cuatrimestre
    costo_total = distancia_total * costo_por_km
    return costo_total

distancia = float(input("Ingrese la distancia de su casa a la Universidad en kilómetros: "))
costo_por_km = float(input("Ingrese el costo por kilómetro: "))
dias_por_semana = int(input("Ingrese la cantidad de días a la semana que viaja a la Universidad: "))

semanas_cuatrimestre = 15

costo_total = costo_traslado(distancia, costo_por_km, dias_por_semana, semanas_cuatrimestre)

print("El costo total de trasladarse durante el cuatrimestre es de:", costo_total, "colones.")
