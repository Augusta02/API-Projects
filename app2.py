import requests
import json
import datetime as dt
import os

base_url = "http://api.weatherstack.com/current"
city= "Lagos"
api_key = os.environ.get("API_KEY")

print(api_key)

url = f"{base_url}?access_key={api_key}&query={city}"
print(url)
response = requests.get(url)

res= response.json()

print(res)

temperature= res['current']['temperature']
res_city = res['location']['name']
print(res_city)
print(temperature)