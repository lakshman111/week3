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
webservice = urlopen(url)
encoded_data = webservice.read()
decoded_data = encoded_data.decode("utf8")
data = json.loads(decoded_data)
