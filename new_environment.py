import requests
import os

base_url = "http://api.weatherstack.com/current"
city ="Lagos"
api_key = os.environ.get("API_KEY")

url = f"base_url?access_key={api_key}&query={city}"

def get_weather():
    response = requests.request("POST", url)

    return response.json()
