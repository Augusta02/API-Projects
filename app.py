from flask import Flask, render_template
import os
import requests


app= Flask(__name__)

api_key = os.environ.get("API_KEY")
base_url= "https://api.weatherapi.com/v1/current.json?"
city = str(input("Enter city: "))
url = f'{base_url}key={api_key}&q{city}'


@app.route('/')  # type: ignore
def index():
    url = f'{base_url}key={api_key}&q{city}'

    print(url)
    

