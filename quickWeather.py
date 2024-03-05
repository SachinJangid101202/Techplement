#! python3

import json
import sys
import requests
import datetime as dt



if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()

location = ' '.join(sys.argv[1:])

url="http://api.openweathermap.org/data/2.5/weather?q=%s&appid=a15b22989bf0a802670ce99af54dc440" % location
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)

data = weatherData['weather']
print('Current weather in %s:' %(location))
print(data[0]['main'], "-",data[0]['description'])

temp= weatherData['main']
print('Temperature is:',temp['temp']-273.15,"C")