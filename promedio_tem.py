import requests
import random
from dotenv import load_dotenv
import os

load_dotenv()
#clave api de OpenWeatherMap
API_KEY = os.getenv("API_KEY")

#lista de ciudades rastrear la temperatura
ciudades = ["Quito", "Guayaquil", "Cuenca", "Loja", "Machala"]

# Días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Número de semanas
semanas = 1  # Usamos 2 semanas como ejemplo


def obtener_temperatura(ciudad):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if response.status_code == 200:
        temperatura = data["main"]["temp"]
        return temperatura
    else:
        print("Error al obtener la temperatura")
        return None
    
# Función para agregar una variación aleatoria a la temperatura
def variar_temperatura(temperatura):
    return temperatura + random.uniform(-3, 2)  # Varia la temperatura en un rango de -3 a +2 grados


# Matriz para almacenar las temperaturas de cada ciudad por día (suponiendo 7 días)
temperaturas = [[[variar_temperatura(obtener_temperatura(ciudad)) for _ in dias_semana] for _ in range(semanas)] for ciudad in ciudades]

# Mostrar las temperaturas obtenidas
print("Temperaturas diarias por ciudad, semana y día:")
for i, ciudad in enumerate(ciudades):
    for semana in range(semanas):
        print(f"{ciudad} - Semana {semana + 1}:")
        for dia, temp in zip(dias_semana, temperaturas[i][semana]):
            print(f"  {dia}: {round(temp,2)}°C")

# Calcular el promedio de temperaturas por ciudad
def calcular_promedio_temperatura(temperaturas, ciudades, semanas, dias_semana):
    for i, ciudad in enumerate(ciudades):
        suma_total = 0
        conteo_dias = 0
        
        # Sumar todas las temperaturas para cada ciudad en todas las semanas
        for semana in range(semanas):
            for dia in range(len(dias_semana)):
                if temperaturas[i][semana][dia] is not None:
                    suma_total += temperaturas[i][semana][dia]
                    conteo_dias += 1
        
        # Calcular el promedio de temperatura
        if conteo_dias > 0:
            promedio = suma_total / conteo_dias
            print(f"El promedio de temperatura en {ciudad} durante el período es {promedio:.2f}°C")
        else:
            print(f"No se pudo calcular el promedio para {ciudad} debido a la falta de datos.")

calcular_promedio_temperatura(temperaturas, ciudades, semanas, dias_semana)
# Output esperado: