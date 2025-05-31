import requests

API_KEY = 'cd4c6c1a6c4f750756ee3e5fcb4d272a'

def get_cordinates(city):
    geo_url = 'http://api.openweathermap.org/geo/1.0/direct'
    params = {
        'q': city,
        'limit': 1,
        'appid': API_KEY
    }

    response = requests.get(geo_url, params=params)
    data = response.json()

    if response.status_code == 200 and data: 
        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon
    else: 
        return None, None
    

def get_weather(lat, lon, city): 
    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY, 
        'units': 'metric'
    }

    print(weather_url)
    response = requests.get(weather_url, params=params)
    data = response.json()

    if response.status_code == 200: 
        print(f"\n📍 Weather in {city.title()}")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"    Wind: {data['wind']['speed']}")
        print(f"☁️ Description: {data['weather'][0]['description']}")
    else:
        print("❌ Weather data not found.")
    
if __name__ == '__main__': 
    city = input("Enter city name: ")
    lat, lon = get_cordinates(city)

    if lat and lon: 
        get_weather(lat, lon, city)
    else: 
        print("❌ Invalid city name or not found.")