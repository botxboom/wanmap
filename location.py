import requests
import json

def findLocation(ip):

    url = "https://api.ipgeolocation.io/ipgeo?apiKey=41b536450a674d3ba0a9846ae1349958&ip={}".format(ip)
    response = requests.request("GET", url )
    result = json.loads(response.text)
    return [result['latitude'], result['longitude']]

