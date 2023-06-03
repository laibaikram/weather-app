import requests

class WeatherAPI:
    def get_weather(self, city):
        # Replace 'YOUR_API_KEY' with your actual API key
        api_key = 'YOUR_API_KEY'
        
        # Make API request
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            weather_info = self.extract_weather_info(data)
            return weather_info
        else:
            raise Exception("Failed to fetch weather information.")
    
    def extract_weather_info(self, data):
        # Extract relevant weather information from API response
        main_weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        
        weather_info = f"Weather: {main_weather}\nDescription: {description}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
        return weather_info

