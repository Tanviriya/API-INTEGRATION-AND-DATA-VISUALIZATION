import requests
import json
import matplotlib.pyplot as plt
import seaborn as sns
# requests → Used to send HTTP requests to the OpenWeatherMap API to fetch weather data.
# json → Used to format and print the JSON response from the API.
# matplotlib.pyplot (plt) → Used for creating the bar chart to visualize weather data.
#seaborn (sns) → An advanced visualization library that enhances the appearance of plots.


#Stores your personal API key required for authentication with OpenWeatherMap.
API_KEY = "c25be446ad0e4831a6e980658bec3d28"

#The API endpoint URL that provides current weather data for a given city.
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Function to fetch weather data
def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Define city
city_name = "Delhi"
weather_data = get_weather(city_name)

if weather_data:
    print(json.dumps(weather_data, indent=4))

    # Extracting key weather parameters
    temp = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    pressure = weather_data["main"]["pressure"]

    print(f"\nWeather Data for {city_name}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")

    # Bar chart visualization defining labels
    labels = ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"]
    values = [temp, humidity, pressure]
#definig the value for bar figure
    plt.figure(figsize=(8, 5))
    sns.barplot(x=labels, y=values, hue=labels, palette="coolwarm", legend=False)
    plt.title(f"Weather Data for {city_name}")
    plt.ylabel("Value")
    plt.show()
#if result are something else then....
else:
    print("City not found! Please enter a valid city name.")
