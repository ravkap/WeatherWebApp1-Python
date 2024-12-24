import requests
from dotenv import load_dotenv
import os
import json
from urllib.parse import quote
from pprint import pprint


load_dotenv()

json_file_path = "C:\PythonPractice\Lesson 21\city.list.json"


def find_city_id(city_name, json_file_path):
    """
    Parse the JSON file to find the city ID based on the city name.
    """
    with open(json_file_path, 'r', encoding='utf-8') as file:
        city_data = json.load(file)
        for city in city_data:
            if city["name"].lower() == city_name.lower():
                return city["id"]
    return None


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name:\n")
    json_file_path = "city_list.json"
    api_key = os.getenv("API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather?appid"

    if " " in city:

        city_id = find_city_id(city, json_file_path)
        if city_id:
            request_url = f"{url}={api_key}&units=imperial&id={city_id}"
        else:
            print(f"City '{city}' not found in the city list JSON file.")
            return
    else:

        encoded_city = quote(city)
        request_url = f"{url}={api_key}&units=imperial&q={encoded_city}"

    print("\nRequest URL:")
    print(request_url)

    response = requests.get(request_url)
    if response.status_code == 200:
        weather_data = response.json()

        pprint(weather_data)
        print(f"\nCurrent Weather for {weather_data['name']}")
        print(f"Current temp is {weather_data['main']['temp']}°F")
        print(f"Feels like {weather_data['main']['feels_like']}°F with {
              weather_data['weather'][0]['description']}.")
    else:
        print(f"Error: Unable to fetch data. HTTP Status Code: {
              response.status_code}")


if __name__ == "__main__":
    get_current_weather()
