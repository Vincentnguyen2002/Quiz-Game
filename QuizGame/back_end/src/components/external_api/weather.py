# Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api
# . Your task is to write a program that asks the user for the name of a municipality and
# then prints out the corresponding weather condition description text and temperature
# in Celsius degrees. Take a good look at the API documentation. You must register for
# the service to receive the API key required for making API requests. Furthermore,
# find out how you can convert Kelvin degrees into Celsius.

import sys
sys.path.append('G:\\Metropolia\\Metropolia\\2023\\Syksy\\SOFTWARE_2\\PROJECT\\QUIZ_PROJECT\\back_end')
from src.config import dbconfig

# https: // openweathermap.org / api
import requests.exceptions
import json
import datetime as dt
from pytz import timezone
# from back_end.config import dbconfig
from src.config import dbconfig


private_key = dbconfig.private_key

#geo_request
# query_string = "London"

# geo_request =f"http://api.openweathermap.org/geo/1.0/direct?q={query_string}&limit=5&appid={private_key}"
# print(geo_request)

# example_request = "http://api.openweathermap.org/geo/1.0/direct?limit=5&appid=28e489100830be62a52cd6f528c12b6c&q=London"
#weather request
# weather_request = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={private_key}"
# # https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={API key}

def get_location(location_name):
    geo_request = (f"http://api.openweathermap.org/geo/1.0/"
                   f"direct?q={location_name}&limit=5&appid={private_key}")
    try:

        response = requests.get(geo_request).json()  #recommend way
        # print(response)
        # if len(response) > 0 and response["cod"] != "400" :
        if isinstance(response,list) and len(response) > 0:
            location =response[0]
            location_lon = location["lon"]
            location_lat = location["lat"]
            location_name = location["name"]

            # print(json.dumps(response[0], indent=2))

            return [location_lon,location_lat,location_name]
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f" Error: {e}")

def get_forecast_at_location(place_name):
    json_response = {}
    location = get_location(place_name)
    # print(f"location: {location}")
    if location == [] :
        return json_response
    else:
        location_lon, location_lat, location_name = location
        unit = "metric"
        # print(f"longitute: {location_lon} - latitute: {location_lat}")

        weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={location_lat}&lon={location_lon}&appid={private_key}&units={unit}"
        try:
            # response = requests.get(request)
            response = requests.get(weather_request).json()  # recommend way
            # print(json.dumps(response,indent=2))
            # location = "Location: "+response['name']
            # coordinate = f"Coordinate: {location_lat} - {location_lon}"

            # print(result_str)
            weather = response["weather"][0]
            # print(weather)
            main_weather = weather["main"]
            description =weather["description"]
            # result_str = result_str + main_weather +"\n" description + "\n""

            # get temperature
            main_temperature= response["main"]
            temp = main_temperature["temp"]
            feels_like = main_temperature['feels_like']

            json_response = {
                "location": location_name,
                "latitude": location_lat,
                "longitude": location_lon,
                "weather": main_weather,
                "weather_description": description,
                "temperature": temp,
                "feels_like":feels_like
            }

            return json_response

        # print(json.dumps(response[0], indent=2))

        # return [location_lon, location_lat]
        except requests.exceptions.RequestException as e:
            print(f" Error: {e}")

def convert_str (string_list) :
    result_str = ""
    for string in string_list:
        result_str = result_str + string + "\n"

    return result_str

def get_json_response(city_name):
    json_response = {}
    response = get_forecast_at_location(city_name)
    if not response:
        response = ""
        # json_response = {city_name: ""}
        # return json_response
    
    json_response = {
        "name" : city_name,
        "value" :response
    }
    return json_response


def get_location_name():
    return input("Type the Location you want to have forecast: ")

def main():
    location_name = get_location_name()
    # result_str_list = get_forecast_at_location(location_name)
    response = get_forecast_at_location(location_name)
    # return object, either {} or with content
    json_response = get_json_response(location_name)
    if json_response == {} :
        print("There is no city with such name!!")
        return
    else:
        print(json_response)
        # print(final_str)

# location_lon, location_lat = get_location(query_string)
# print(f"longitute: {location_lon} - latitute: {location_lat}")
# print(get_forecast_at_location(query_string))

if __name__ == "__main__":
    command = "1" # cause program to go to loop
    while command  == "1":
        main()
        command = input("Do you want to continue? (1 - continue, else to quit) ")
    # query_string = "New York"
    # get_forecast_at_location(query_string)
    # result_string_list = get_forecast_at_location(query_string)
    # print(convert_str(result_string_list))
