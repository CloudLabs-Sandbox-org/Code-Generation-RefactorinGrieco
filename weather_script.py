import requests

def get_weather():
    # Coordenadas de la ciudad de Campana, Provincia de Buenos Aires
    lat = -34.1687
    lon = -58.9593
    api_key = "e3d9891eb21b4af8a782f460f9ff99cc"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la respuesta contiene un error HTTP
        weather_data = response.json()

        # Extraer información relevante
        city = weather_data.get("name", "Desconocido")
        temp = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]

        print(f"Clima en {city}:")
        print(f"Temperatura: {temp}°C")
        print(f"Descripción: {weather_description.capitalize()}")

    except requests.exceptions.RequestException as e:
        print(f"Error al consultar el clima: {e}")
    except KeyError:
        print("Error al procesar los datos del clima.")

if __name__ == "__main__":
    get_weather()