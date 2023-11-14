import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # metric units for Celsius

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data. Status Code: {response.status_code}")
        return None

def display_weather(weather_data):
    if weather_data:
        main_info = weather_data["main"]
        temperature = main_info["temp"]
        description = weather_data["weather"][0]["description"]

        print(f"Weather: {description}")
        print(f"Temperature: {temperature}°C")
    else:
        print("No weather data to display.")

def main():
    api_key = "914d9fce7d628316158eb5fe3057931b"
    city = input("Kindly enter your city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
