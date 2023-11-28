from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import paho.mqtt.subscribe as subscribe

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    body = body.lower()
    print("This is the text body: " + body)
    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'temp1':

        # Subscribe to topic and get latest data point
        msg = subscribe.simple("temp1", hostname="<insert MQTT Broker domain name or ip address>")

        # Message formatting
        msg = str(msg.payload)
        print("This is the temperature: " + msg)
        #msg = msg[len(msg) - 6: -1]
        msg = msg[msg.rfind('#'):]
        msg = msg[1:-1]
        # Send formatted message back to user
        resp.message(msg)

    elif body == 'temp2':

        # Subscribe to topic and get latest data point
        msg = subscribe.simple("temp2", hostname="<insert MQTT Broker domain name or ip address>")

        # Message formatting
        msg = str(msg.payload)
        print("This is the temperature: " + msg)
        #msg = msg[len(msg) - 6: -1]
        msg = msg[msg.rfind('#'):]
        msg = msg[1:-1]
        # Send formatted message back to user
        resp.message(msg)

    else:
        resp.message('Invalid Input')

    return str(resp)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True, host='<insert webapp domain name or ip address>', port=5002)
