from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

import requests
from datetime import date, timedelta

API_KEY = 'UkZXQJvt2dXeweqdgNBdBghnfVwDTElEoJnCbqoT'

apod_parameters = {
    'api_key': API_KEY,
    'date': date.today()
}
response = requests.get("https://api.nasa.gov/planetary/apod", params = apod_parameters)
data = response.json()
title, explanation, url = data['title'], data['explanation'], data['url']

def caesar(plaintext, shift):
    output = ""
    for ch in plaintext:
        output += chr(ord(ch) + shift)
    return output

title = caesar(title, 10)
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
        
    if not responded:
        msg.body('Error, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run(port=4000)