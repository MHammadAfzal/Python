import urllib.request, urllib.parse, urllib.error
import json

# ! APIs in PYTHON

serviceUrl = "http://maps.googleapis.com/maps/api/geocode/json?"
while True:
    address = input("What's Address? ")
    if len(address) < 1:
        break

    url = serviceUrl + urllib.parse.urlencode({"address": address})

    print("Retrieving", url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("======Failure======")
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)

    location = js["results"][0]["formatted_address"]
    print(location)

    # We will get no response as we need API key to get response which we haven't purchased
    # * Go to p.py for further clarification