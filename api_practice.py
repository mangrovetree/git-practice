import requests

def get_weather_forecast(latitude, longitude):
    # plugging in parameters to the url
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(api_url)
    # if status of api is active, run
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


# converting all inputs to floats
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))

forecast_data = get_weather_forecast(latitude, longitude)

if forecast_data:
    print(forecast_data)
else:
    print("Error occurred while fetching data from the API.")


