from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

app = Flask(__name__)

# Your Twilio Account SID and Auth Token
account_sid = 'ACadb978b44431b43d68d9b27250fe80b7'
auth_token = '3327609ed7cc170a052942ca65f5fff1'
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
        from_='your_twilio_phone_number'
    )
    return f'Call initiated. SID: {call.sid}'

if __name__ == '__main__':
    app.run(port=5000)
