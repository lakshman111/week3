# Divvy Bikes
#
# Here's an example of how to retrieve the list of Divvy bike stations:

import json
import urllib.request
# from urllib.request import urlopen

webservice_url = "http://www.divvybikes.com/stations/json"
json_data = json.loads(urllib.request.urlopen(webservice_url).read().decode("utf8"))
