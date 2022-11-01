import requests
from datetime import datetime

latitude = 39.143440
longitude = 77.201370

parameters = {
    'latitude': latitude,
    'longitude': longitude,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today", params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]['sunset'].split('T')[1].split(':')[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)