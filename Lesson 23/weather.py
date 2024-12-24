from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Las Vegas"):

    url = ("https://api.openweathermap.org/data/2.5/weather?appid")

    request_url = f"{url}={os.getenv("API_KEY")}&units=imperial&q={city}"

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # check for empty string or sting with only spaces
    if not bool(city.strip()):
        city = "Las Vegas"
    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
