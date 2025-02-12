import requests

API_KEY = "b7c57d2e62261aa20f697a4a78792bbd"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# get weather method 
def get_weather(city): 
    params = {"q" : city, # city entered by user
              "appid": API_KEY, # api key for authentication
              "units": "imperial"} # use 

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

        wind_speed = data['wind']['speed']

        # display weather information 
        print(f"\n🌤️ Weather in {city.capitalize()}:")  # City name with first letter capitalized
        print(f"   - {weather_description}")  # Weather description
        print(f"   - Temperature: {temp}°F (Feels like {feels_like}°F)")  # Current temp and feels like
        print(f"   - Humidity: {humidity}%")  # Humidity percentage
        print(f"   - Wind Speed: {wind_speed} mph")  # Wind speed in meters per second

    else: 
        print("\n⚠️ City not found. Please try again.")

# run the program when executed
if __name__ == '__main__': 
    # get city from user
    city = input("Enter city name: ")

    # get the weather 
    get_weather(city)