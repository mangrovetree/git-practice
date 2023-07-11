from api_practice import get_weather_forecast

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("run")

# converting all inputs to floats
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))

forecast_data = get_weather_forecast(latitude, longitude)

if forecast_data:
    print(forecast_data)
else:
    print("Error occurred while fetching data from the API.")