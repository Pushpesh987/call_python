from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Twilio credentials from environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(account_sid, auth_token)

@app.route('/twilio/voice', methods=['POST'])
def voice():
    response = VoiceResponse()
    response.say("Hello, this is a Twilio voice call!")
    return Response(str(response), content_type='application/xml')

@app.route('/twilio/make-call', methods=['POST'])
def make_call():
    to_phone_number = request.form.get('to')
    call = client.calls.create(
        twiml='<Response><Say>Hello, this is an outbound Twilio voice call!</Say></Response>',
        to=to_phone_number,
        from_=twilio_phone_number
    )
    return f'Call initiated. SID: {call.sid}'

if __name__ == '__main__':
    app.run(port=5000)
