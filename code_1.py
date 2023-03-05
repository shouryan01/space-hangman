from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

import requests
from datetime import date, timedelta

apod_parameters = {
    'api_key': API_KEY,
    'date': date.today()
}
response = requests.get("https://api.nasa.gov/planetary/apod", params = apod_parameters)
data = response.json()
title, explanation, url = data['title'], data['explanation'], data['url']

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
        msg.body('Hangman game')
        responded = True
        
    if not responded:
        msg.body('Error, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run(port=4000)