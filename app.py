from flask import Flask, render_template
import os
import requests


app= Flask(__name__)
if __name__ == "__main__":
    app.run()

app.config['DEBUG'] = True

base_url= "https://api.weatherstack.com/current"
city = "Lagos"
api_key= os.environ.get("API_KEY")



@app.route('/', methods=['GET'])  # type: ignore
def index():
    
    url = f'{base_url}?access_key={api_key}&query={city}'
    print(url)
    r= requests.get(url)
    new_res= r.json()
    print(new_res)

    
    weather= {
        'city': new_res['location']['name']['country'],
        'temperature': new_res['current']['temperature'],
        'feels_temp' : new_res['current']['feelslike'],
        'description': new_res['current']['weather_descriptions'],
        'cloud': new_res['current']['cloudcover'],
    }
    print(weather)
    return render_template('index.html', weather=weather)
    
