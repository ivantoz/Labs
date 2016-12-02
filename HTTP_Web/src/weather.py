import json
import requests

print ("\n\nWelcome to this simple Commandline Weather App \n", "-"*46)
city = input("Enter the name of the City you want to query weather information: ")
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=857013fd87ce20b5e5305b3f35bab216")
print ("\n", response.status_code, response.reason, "- The Connection was successful!\n")



data = json.loads(response.text)

print ("ID:", data['id'], "\nCity:", data['name'], "\nCountry Code:", data['sys']['country'], "\nCoordinates: ", str(data['coord']['lon']) + ", " + str(data['coord']['lat']), "\nDate:", data['dt'], "\nDescription:", data['weather'][0]['description'], "\nHumidity :", data['main']['humidity'], "\nPressure :", data['main']['pressure'], "\nWind Speed :", data['wind']['speed'], "\nWind Deg :", data['wind']['deg'], "\nTemperature:", str(data['main']['temp'] - 273) + u"\N{DEGREE SIGN}C")
