from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
   

    msg = request.form.get('Body')

    url = 'https://api.worldpostallocations.com/pincode/'+msg+'/IN'

    response_API = requests.get(url)

    data = response_API.text

    parse_json = json.loads(data)
    #print(data)

    # Create reply
    resp = MessagingResponse()
    resp.message("City is : {}".format(parse_json["result"][0]["district"]))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)