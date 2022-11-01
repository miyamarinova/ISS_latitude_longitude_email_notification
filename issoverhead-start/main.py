import requests
from datetime import datetime
import smtplib
import time

my_email = 'mariayoana.marinova@gmail.com'
my_password = "tmahgoyljurllnao"


is_dark = True
iss_above_me = False

MY_LAT = 39.143440 # Your latitude
MY_LONG = -77.201370 # Your longitude

def is_iss_above_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


def send_email_if_ISS_above_me():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="miyamarinova@gmail.com",
            msg="Subject: THE ISS IS ABOVE YOU\n\nLOOK UP"
        )

while True:
    time.sleep(60)
    if iss_above_me and is_dark:
        send_email_if_ISS_above_me()

