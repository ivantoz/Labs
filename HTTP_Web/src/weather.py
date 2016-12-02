import json
import requests
import datetime
from HTTP_Web.src.utilities import degrees_to_direction
from HTTP_Web.src.utilities import bcolors

underline = '-'*55
print(bcolors.HEADER,'\t', underline, bcolors.ENDC)
heading ='\n\t\tWelcome to this simple Commandline Weather App \n '
print(bcolors.HEADER, heading.upper(), bcolors.ENDC)
print(bcolors.HEADER,'\t', underline, bcolors.ENDC)
subheading = '\t\t\t\tThe ultimate weather app'
print(bcolors.OKGREEN, subheading,bcolors.ENDC)

print('\t', bcolors.BOLD)
city = input("Enter the name of place to search: ")
print(bcolors.ENDC)
city = city.strip()
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=857013fd87ce20b5e5305b3f35bab216")

if response.status_code ==200:
    msg = '- The Connection was successful!\n'
    print(bcolors.OKGREEN,response.status_code, response.reason, msg, bcolors.ENDC)



data = json.loads(response.text)

description = data['weather'][0]['description'].capitalize()
dt = datetime.datetime.fromtimestamp(data['dt'])
date_obtained = dt.strftime("%A, %d %B %Y %I:%M%p")
temperatue = str(data['main']['temp'] - 273) + u"\N{DEGREE SIGN}C"
pressure = data['main']['pressure']
humidity = data['main']['humidity']
wind_direction = degrees_to_direction(data['wind']['deg'])
wind_speed = data['wind']['speed']
sr = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
sunrise = sr.strftime("%I:%M%p")
st = datetime.datetime.fromtimestamp(data['sys']['sunset'])
sunset = st.strftime("%I:%M%p")
country_code = data['sys']['country']
cordinates = str(data['coord']['lon']) + ", " + str(data['coord']['lat'])


print("\n")
print('\t', bcolors.HEADER, 'Weather  in ', city.capitalize(), ',', country_code, bcolors.ENDC, '\n')
print('\t', bcolors.OKBLUE, 'Description\t:', bcolors.ENDC, bcolors.OKGREEN, description, bcolors.ENDC)
print('\t', bcolors.OKBLUE, 'Date obtained\t:', bcolors.ENDC, bcolors.OKGREEN, date_obtained, bcolors.ENDC)
print('\t', bcolors.OKBLUE, 'Temperature\t:', bcolors.ENDC, bcolors.OKGREEN, temperatue, bcolors.ENDC)
print('\t', bcolors.OKBLUE, 'Pressure\t\t:', bcolors.ENDC, bcolors.OKGREEN, pressure, ' hpa', bcolors.ENDC)
print('\t', bcolors.OKBLUE, 'Humidity\t\t:', bcolors.ENDC, bcolors.OKGREEN, humidity, '%', bcolors.ENDC)
print('\t', bcolors.OKBLUE, 'Wind Direction:', bcolors.ENDC, bcolors.OKGREEN, wind_direction, bcolors.ENDC)
print('\t', bcolors.OKBLUE, 'Wind Speed\t:', bcolors.ENDC, bcolors.OKGREEN, wind_speed, ' m/s', bcolors.ENDC)
print('\t', bcolors.OKBLUE, 'Sunrise\t\t:', bcolors.ENDC, bcolors.OKGREEN, sunrise, bcolors.ENDC)
print('\t', bcolors.OKBLUE, 'Sunset\t\t:', bcolors.ENDC, bcolors.OKGREEN, sunset, bcolors.ENDC)
print('\t', bcolors.OKBLUE, 'Cordinates\t:', bcolors.ENDC, bcolors.OKGREEN, cordinates, bcolors.ENDC)

print('\n', bcolors.BOLD, "Powered by http://openweathermap.org/", bcolors.ENDC)

