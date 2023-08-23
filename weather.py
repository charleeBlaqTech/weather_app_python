import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print(f'\n*** Get current Weather conditions ☁☁☁ ***\n')

    city= input("\nPlease enter a city name:\n")
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    # print(request_url)
    weather_data= requests.get(request_url).json();
    # pprint(weather_result)
    city_name       = weather_data["name"]
    country         = weather_data["sys"]['country']
    current_temp    = weather_data["main"]['temp']
    weather_desc    = weather_data["weather"][0]['description']

    print(f"\n\nToday in {city_name} city {country},\nWith a temperature of {current_temp} degree celcius\nFeels like {weather_data['main']['feels_like']} and {weather_desc}.☁☁🌧🌨 ☁☁☁\n");
    print("\nThanks for using our Services..... 😊😊😊")




if __name__ == "__main__":
    get_current_weather()