"""How python communicates with internet,https://home.openweathermap.org/"""
import requests
import sys
# API keys-->(username-->my api keys)
API_key = "d5d433d3fdbf48e399159eb442ce3b45"
COUNTRY_code = input("Please enter valid county code:")
ZIP_code = input("please enter valid zip code: ")
# what url python will connect to!(below url)--> API-->Current Weather Data--> Built-in API request by ZIP code)
url = f"https://api.openweathermap.org/data/2.5/weather?zip={ZIP_code},{COUNTRY_code}&appid={API_key}"
print(url)
# How to connect to url
connect = requests.get(url)
# 200--> successful status code for connection.
# The output is in json format, just used the dic for key,value pair.
# just ctrl+click to view the link.
# sys module is used to verify that our script ran successfully or not(via echo $?)
if connect.status_code != 200:
    print(connect.json()["message"])
    print(sys.exit(1))
else:
    print(connect.json()["weather"])