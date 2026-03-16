import requests
from twilio.rest import Client
import os

weather_api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

params = {
    "lat":21.309919,
    "lon":-157.858154,
    "cnt":4,
    "appid":weather_api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast?", params=params)
response.raise_for_status()

will_rain = False
weather_data = response.json()
data = weather_data["list"]
for dt_list in data:
    weather_id = dt_list["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True
if will_rain:
    print("Rain")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="Bring an umbrella!",
        to="whatsapp:+16812830298"
    )
    print(message.status)
