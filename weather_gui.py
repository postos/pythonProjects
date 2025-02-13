import tkinter as tk
from tkinter import messagebox
from getWeather import get_weather 

def fetch_weather():
        
    city = city_entry.get().strip()
    state = state_entry.get().strip()
    country = country_entry.get().strip()

    if not city or not state:
        messagebox.showwarning("Input Error", "Please enter both a city and state.")
        return

    data = get_weather(city, state, country)  # Call API function

    if data: 
        # extract weather description 
        weather_description = data['weather'] [0]['description'].capitalize()

        # extract weather details 
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        min_temp = data['main']['temp_min']
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
        print("\n⚠️ Location not found. Please try again.")

# GUI Setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

tk.Label(root, text="Enter City:").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Label(root, text="Enter State (e.g., NY, CA):").pack()
state_entry = tk.Entry(root)
state_entry.pack()

tk.Label(root, text="Enter Country (e.g., US, EU):").pack()
country_entry = tk.Entry(root)
country_entry.pack()

submit_button = tk.Button(root, text="Get Weather", command=fetch_weather)
submit_button.pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()