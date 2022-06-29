import requests
import smtplib

# API key
api_file = open("api-key.txt", "r")
api_key = api_file.readline()
api_file.close()

# home address input
source = input("Enter a home address\n")

# work address input
destination = input("Enter a work address\n")

# base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# get response
r = requests.get(url + "origins=" + source
                 + "&destinations=" + destination + "&key=" + api_key)

# return time as text and as seconds
time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

# print the travel time
print("\nThe total travel time from home to work is", time)