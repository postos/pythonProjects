import requests
import tkinter as tk
from tkinter import messagebox
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY") # Retrieves the API key from the environment variable set in ~/.zshrc
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# get weather method 
def get_weather(city, state, country): 
    location = f"{city}, {state}, {country}"
    params = {"q" : location, # city entered by user
              "appid": API_KEY, # api key for authentication
              "units": "imperial"} # use 
    if not city: 
        messagebox.showwarning("Input error, please enter a city name.")
        return

    # make API request 
    response = requests.get(BASE_URL, params=params)

    # check response from API
    if response.status_code == 200: 
        data = response.json() # convert the json response into python dictionary 

        # extract weather description 
        weather_description = data['weather'] [0]['description'].capitalize()

        # extract temp details 
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']

        # extract humidity %
        humidity = data['main']['humidity']

        # get wind speed 
        wind_speed = data['wind']['speed']

        # get low temp for the day
        min_temp = data['main']['temp_min']

        # get high temp for the day
        max_temp = data['main']['temp_max']

        # display weather information 
        print(f"\n🌤️  Weather in {city.title()}, {state.upper()}:")  # City name with first letter capitalized
        print(f"   - {weather_description}")  # Weather description
        print(f"   - Temperature: {temp}°F (Feels like {feels_like}°F)")  # Current temp and feels like
        print(f"   - Low: {min_temp}°F ")
        print(f"   - High: {max_temp}°F ")
        print(f"   - Humidity: {humidity}%")  # Humidity percentage
        print(f"   - Wind Speed: {wind_speed} mph")  # Wind speed in meters per second

    else: 
        print("\n⚠️ City not found. Please try again.")

# run the program when executed
if __name__ == '__main__': 
    # get city from user
    city = input("Enter city name: ")
    state = input("Enter state abbreviation (e.g. NY, CA): ")
    country = input("Enter country abbreviation: (e.g US, CA)")

    # get the weather 
    get_weather(city, state, country)