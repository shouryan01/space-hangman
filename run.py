from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

import requests
from datetime import date
import random
import string

API_KEY = 'UkZXQJvt2dXeweqdgNBdBghnfVwDTElEoJnCbqoT'

apod_parameters = {
    'api_key': API_KEY,
    'date': date.today()
}
response = requests.get("https://api.nasa.gov/planetary/apod", params = apod_parameters)
data = response.json()
title, explanation, url = data['title'], data['explanation'], data['url']

def caesar(plaintext):
    plaintext = plaintext[::-1]
    p1 = plaintext[:len(plaintext)//2]
    p2 = plaintext[len(plaintext)//2:]
    return ''.join(random.choices(string.ascii_letters, k=5)) + plaintext + ''.join(random.choices(string.ascii_letters, k=5))

title = caesar(title)
title = title.replace(' ', '%20')

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'picture' in incoming_msg:
        # return a space pic
        msg.media(url)
        responded = True
    if 'describe' in incoming_msg:
        msg.body(explanation)
        responded = True
    if 'hangman' in incoming_msg:
        msg.body('https://shouryan01.github.io/space-hangman/?title={}'.format(title))
        responded = True
    if 'revolution' in incoming_msg:
        msg.body('Revolution is the movement of a planet around the Sun. Check this link out for an AR experience! https://adobeaero.app.link/tZVT9zeaVxb')
        responded = True
    if 'far' in incoming_msg:
        msg.body('The Moon is 238,900 mi away from the Earth. Check this link out for an AR experience! https://adobeaero.app.link/w4iJ47ioVxby')
        responded = True
    if 'face' in incoming_msg:
        msg.body('The Moon orbits Earth once every 27.3 days and spins on its axis once every 27.3 days. This means that although the Moon is rotating, it always keeps one face toward us. Check this link out for an AR experience! https://adobeaero.app.link/zzecFx0oVxb')
        responded = True
    if 'sun' in incoming_msg:
        msg.body('The Sun is Sun is 864,000 miles in diameter. Check this link out for an AR experience! https://adobeaero.app.link/Bwsa8XhpVxb')
        responded = True
    if 'jupiter' in incoming_msg:
        msg.body('Jupiter is the largest planet in the Solar System, at a radius of 43,441 mi. Check this link out for an AR experience! https://adobeaero.app.link/PFBFPXzpVxb')
        responded = True
        
    if not responded:
        msg.body('Error, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run(port=4000)