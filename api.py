from flask import Flask, request, render_template, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from intents import fallback_intent, getLocation
import random, os, requests
from GMapsKey import key
from gmaps import eachplace
import googlemaps

app = Flask(__name__)
key = key()
#os.environ.get("PLACES_API_KEY")
location_fallback = ['What kind of restaurant are you seeking?', 'What kind? Nearby, Cheap or The best?']
welcome = ['hello', 'what\'s up', 'hey','hi', 'what\'s happening?']
near = ['near', 'nearby']
cheap = ['cheap', 'good for my pockets']
good = ['good', 'top rated']

intro_resp = ['''Hey! Welcome to Crave! This interactive platform connects you to the top foodies in the world! We provide you with the best food places where ever you are. The instructions are simple:
1. Save our number in your Phone as Crave.
2. Text us and tell us what type of food you are craving!

This is from python''', '''
Welcome to Crave! Are you ready to get some food for today?
1. Save our number in your Phone as Crave.
2. Text us and tell us what type of food you are craving!
''']

search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url = "https://maps.googleapis.com/maps/api/place/details/json"

@app.route('/', methods=['GET'])
def retreive():
    return render_template('layout.html', title="GET data from Google Maps")

@app.route('/sms', methods=['GET','POST'])
def sms():
    num = request.form['From']
    msg = request.form['Body'].lower()
    resp = MessagingResponse()
    #welcome intent
    if any(word in msg for word in welcome):
        if any(near_word in msg for near_word in near):
            resp.message('These are the location of places near you!')
            print(str(msg.split()))
            return str(resp)
        elif  any(cheap_word in msg for cheap_word in cheap):
            resp.message('These are the location of places that are low cost to you!')
            return str(resp)
        elif any(good_word in msg for good_word in good):
            resp.message('These are the best places in town!')
            return str(resp)
        else:
            location_fallback[random.randint(0,1)]
        resp.message(intro_resp[random.randint(0, 1)])
        print(str(msg.split()))
        return str(resp)
    else:
        resp.message(fallback_intent())
        print(str(msg))
        return str(resp)

def hasZipCode(code):
    if code > 9999 && code < 10000:
        print('This is a valid zip code')
        return True
    else:
        print('Please enter a valid Zip Code')
        return False

def getUserZipCode(sys_zip):
    if int(msg.split()):
        sys_zip = int(msg.split())
        if hasZipCode(sys_zip):
            return findPlaceByZip(sys_zip, 4000)



# a specific location via link
@app.route('/sendRequest/<string:query>')
def results(query):
    search_payload = {"key":key, "query":query}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()

    place_id = search_json["results"][0]["place_id"]
    details_payload = {"key":key, "placeid": place_id}
    details_resp = requests.get(details_url,  params=details_payload)
    details_json = details_resp.json()

    url = details_json["result"]["url"]

    return jsonify({"result": url})

if __name__ == '__main__':
    app.run(debug=True)
