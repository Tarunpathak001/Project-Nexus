import requests
from ..config import Config
class WeatherService:
    def get_weather(self, city):
        if not city:
             return {"error": "Please enter a city name."}
        search_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Config.API_KEY}&units=metric"
        try:
            response = requests.get(search_url)
            response.raise_for_status()
            weather_data = response.json()
            return {
                "main": weather_data.get('weather', [{}])[0].get('main', 'N/A'),
                "description": weather_data.get('weather', [{}])[0].get('description', 'N/A'),
                "temp": weather_data.get('main', {}).get('temp', 'N/A')
            }
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "not_found": city}
weather_service = WeatherService()