from flask import Flask, render_template
import os
import requests


app= Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])  # type: ignore
def index():
    api_key= os.environ.get("API_KEY")
    base_url= "http://api.weatherstack.com/current"
    print(base_url)
    city = "Lagos"
    url = f'{base_url}access_key={api_key}&query={city}'
    print(url)

    r= requests.get(url)
    new_res= r.json()
    
    temperature= new_res['current']['temperature']

    return render_template('index.html')
    
