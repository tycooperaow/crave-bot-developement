from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import random

location_fallback = ['What kind of restaurant are you seeking?', 'What kind? Nearby, Cheap or The best?']

def fallback_intent():
    fallback_phrase = ['What was that?', 'I don\'t understand', 'Come again?', 'What did you say?']
    return fallback_phrase[random.randint(0,3)]

def getLocation():
    near = ['near', 'nearby']
    cheap = ['cheap', 'good for my pockets']
    good = ['good', 'top rated']
    num = request.form['From']
    msg = request.form['Body'].lower()
    resp = MessagingResponse()
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
