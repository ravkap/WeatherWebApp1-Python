import requests
from dotenv import load_dotenv
import os
from pprint import pprint


load_dotenv()


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name:\n")
    url = "https://api.openweathermap.org/data/2.5/weather?appid"

    request_url = f"{url}={os.getenv("API_KEY")}&units=imperial&q={city}"

    print(request_url)
    weather_data = requests.get(request_url).json()

    pprint(weather_data)

    print(f"Current Weather for {weather_data["name"]}")
    print(f"Current temp is {weather_data["main"]["temp"]}")
    print(f"Feels like {weather_data["main"]["feels_like"]} and {
          weather_data["weather"][0]["description"]}.")


if __name__ == "__main__":
    get_current_weather()


# how to escape a space in python
# function for city as parameter, check if city has a space value, if yes parse json file for city id and pass it back, then pass id to url
