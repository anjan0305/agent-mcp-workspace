def get_weather_reporter (city_name:str):
    if city_name=="Delhi":
        return "It is hot and 40°C"
    elif city_name=="London":
        return "It is rainy and 15°C"
    else:
        return "Weather data not available for this city."


print(get_weather_reporter("Kolkata"))