import requests

def get_weather_forecast(latitude, longitude):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))

forecast_data = get_weather_forecast(latitude, longitude)

if forecast_data:
    print(forecast_data)
else:
    print("Error occurred while fetching data from the API.")


