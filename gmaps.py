import googlemaps
import pprint
import time
from GMapsKey import key

api_key = key()

gmaps = googlemaps.Client(key = api_key)
place_result = gmaps.places_nearby(location=['34, -123'], radius= 40000, open_now = False, type = 'cafe')

#define search
def findPlaceByZip(user_zipcode, user_radius):
    myplace_id = place['place_id']
    zipcode = ['address_components'][7]["long_name"]
    locationByZip = gmaps.place(place_id=myplace_id, fields=zipcode)

    return locationByZip

#pprint.pprint(place_result)

#pauses the script
time.sleep(4)

#place_result_next = gmaps.places_nearby(page_token = place_result['next_page_token'])
#pprint.pprint(place_result_next)
def eachplace():
    for place in place_result['results']:
        #define place
        myplace_id = place['place_id']

        #define the fields we want to send back
        my_fields = ["url", "name", "formatted_phone_number", "type"]

        #make a request for the details
        place_details = gmaps.place(place_id=myplace_id, fields=my_fields)

        #print the results
        return str(place_details)

print(eachplace())
