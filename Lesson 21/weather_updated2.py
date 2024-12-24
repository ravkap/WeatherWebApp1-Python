import requests
from dotenv import load_dotenv
import os
import json
from urllib.parse import quote
from pprint import pprint


load_dotenv()


def search_city_variants(city_name, json_file_path):
    """
    Search the JSON file for all instances of the city name, and return possible country options.
    """
    city_variants = []
    with open(json_file_path, 'r', encoding='utf-8') as file:
        city_data = json.load(file)
        for city in city_data:
            if city["name"].lower() == city_name.lower():
                city_variants.append(
                    {"id": city["id"], "country": city["country"], "state": city.get("state", "")})
    return city_variants


def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')
    city = input("\nPlease enter a city name:\n")
    json_file_path = "city_list.json"  # Replace with the path to your city JSON file
    api_key = os.getenv("API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather?appid"

    # Search the JSON file for possible city-country matches
    city_variants = search_city_variants(city, json_file_path)

    if len(city_variants) == 0:
        print(f"City '{city}' not found in the city list JSON file.")
        return
    elif len(city_variants) == 1:
        # Only one match found, use it directly
        selected_city = city_variants[0]
    else:
        # Multiple matches found, ask user to specify
        print("\nMultiple locations found. Please specify:")
        for idx, variant in enumerate(city_variants, start=1):
            state_info = f", {variant['state']}" if variant['state'] else ""
            print(f"{idx}: {variant['name']}{
                  state_info}, {variant['country']}")

        choice = input(
            "\nEnter the number corresponding to the correct location, or press Enter to cancel:\n")
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(city_variants):
            print("Invalid choice or cancelled. Exiting.")
            return
        selected_city = city_variants[int(choice) - 1]

    # Use the selected city's ID to construct the API request
    request_url = f"{url}={api_key}&units=imperial&id={selected_city['id']}"

    print("\nRequest URL:")
    print(request_url)

    # Make the API request
    response = requests.get(request_url)
    if response.status_code == 200:
        weather_data = response.json()

        # Display weather information
        pprint(weather_data)
        print(f"\nCurrent Weather for {weather_data['name']}, {
              weather_data['sys']['country']}")
        print(f"Current temp is {weather_data['main']['temp']}°F")
        print(f"Feels like {weather_data['main']['feels_like']}°F with {
              weather_data['weather'][0]['description']}.")
    else:
        print(f"Error: Unable to fetch data. HTTP Status Code: {
              response.status_code}")


if __name__ == "__main__":
    get_current_weather()
