import requests
import json

#Read A web page
#response = requests.get("https://twitter.com/dna")
#url = "http://www.json-generator.com/api/json/get/chQLxhBjaW?indent=2"
url = "https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(cityName)
response = requests.get(url)
print(response.text)

print()
"""
data = json.loads(response.text)
print(data["bookstore"])
print(data["bookstore"][1]["name"])

1c8021d59cf8537f798250dc7ee8f5a4
"""