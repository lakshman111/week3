# Geocoding

# Determine the geocoordinates of these famous Chicago landmarks:
#
# United Center
# Millenium Park
# Sears Tower
# Young Memorial Building
#
# You can:
# - web: http://maps.google.com combined with the "What's Here?" trick
# - webservice: https://developers.google.com/maps/documentation/geocoding/intro

from os import system
import json
from urllib.request import urlopen

url = "https://maps.googleapis.com/maps/api/geocode/json?address=Millenium+Park,+Chicago,+IL"
# URLopen basically types the website in and loads it
webservice = urlopen(url)
# .read() then pulls the JSON from the page
encoded_data = webservice.read()
# utf8 makes sure that I include all characters
decoded_data = encoded_data.decode("utf8")
# now parse the JSON so that it isn't a string anymore
data = json.loads(decoded_data)

print("Millenium Park is at", data['results'][0]['geometry']['location']['lat'])

# to look at the keys
# data.keys()

# to look at the values
# data['results']

# digging deeper
# data['results'][0].keys()

