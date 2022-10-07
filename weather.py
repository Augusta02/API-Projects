import requests 
import datetime as dt
import json



# base_url = "http://dataservice.accuweather.com/locations/v1/cities/NG/search?"
# api_key = "Mm0m68Ter6sZPSGGdaNSbCZdeXXSszlQ"
# city = "Lagos"
# language = "en-us"



# url = base_url + "apikey=" + api_key + "&q=" + city + "&language=" + language 
# print(url)

# response = requests.get(url)
# print(response.status_code)
# print(response.json())


base_url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"
key = "4607"
api_key = "Mm0m68Ter6sZPSGGdaNSbCZdeXXSszlQ"
language = "en-us"


# convert fahreheit to celsius
# def fahrenheit_celsius(fahrenheit):
#     fahrenheit = [i['Value'] for i in forecast_api['DailyForecasts']]
#     celsius = ((fahrenheit) - 32) * (5 / 9)
#     print(float(celsius))
# fahrenheit_celsius(fahrenheit=i['Value'])


forecast_api = base_url + key + "?apikey=" + api_key + "&language=" + language
response = requests.get(forecast_api)
res = response.json()

# temp_fa= response[1]['Value']
# print(temp_fa)

sun_rise= res['DailyForecasts']['Sun']['Rise']
print(sun_rise)


# temp_fa= response['DailyForecasts']['Temperature']['Value']
# temp_celsius = fahrenheit_celsius(temp_fa)
# print(temp_celsius)


# def url_link(session, city):
#     baseUrl = "https://api.weatherapi.com/v1/current.json?"
#     city: