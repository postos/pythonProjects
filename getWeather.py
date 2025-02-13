import requests
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY") # Retrieves the API key from the environment variable set in ~/.zshrc
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# get weather method 
def get_weather(city, state, country): 
    location = f"{city}, {state}, {country}"
    
    params = {"q" : location, # city entered by user
              "appid": API_KEY, # api key for authentication
              "units": "imperial"} # use 

    # make API request 
    response = requests.get(BASE_URL, params=params)

    # check response from API
    if response.status_code == 200: 
        return response.json() # convert the json response into python dictionary 
    else: 
        return None

      