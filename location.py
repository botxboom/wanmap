import requests
import json
from config import geoKey

def findLocation(ip):

    url = "https://api.ipgeolocation.io/ipgeo?apiKey={}&ip={}".format(geoKey, ip)
    response = requests.request("GET", url )
    result = json.loads(response.text)
    return [result['latitude'], result['longitude']]

