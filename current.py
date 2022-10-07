
import requests
import json
import datetime as dt
import os

api_key = os.environ.get("API_KEY")
# print(api_key)



base_url = "https://api.weatherapi.com/v1/current.json?"


user_input= str(input("Enter city: "))



url = base_url + "key=" + api_key + "&q=" + user_input
response = requests.get(url)

res = response.json()

temperature = res['current']['temp_c']
feels_temp = res['current']['feelslike_c']
humidity = res['current']['humidity']
description = res['current']['condition']['text']
local_time = res['location']['localtime']
cloud = res['current']['cloud']
uv = res['current']['uv']
windspeed= res['current']['wind_mph']


print(f"Time in {user_input}: {local_time}")
print(f'Temperature in {user_input}: {temperature}°C')
print(f"Temperature in {user_input} feels like: {feels_temp}°C")
print(f"Humidty in {user_input}: {humidity}%")
print(f"Wind Speed in {user_input}: {windspeed}m/h")
print(f"General Weather in {user_input}: {description}")

