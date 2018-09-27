from flask import Flask, request,render_template, redirect
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.jwt.client import ClientCapabilityToken
import re


app = Flask(__name__)

caller_id="+19015988438"

callers={
    "+19013412717": "Butt head",
    "+19012163984": "Doctor Rosen Rosen",
    "+19014966161": "General Noriega",
}


@app.route("/voice",methods=['GET','POST'])
#def voice(): 
 #   dest_number=request.values.get('PhoneNumber',default_client)
  #  resp=VoiceResponse()

   # with resp.dial(callerId=caller_id) as r:
    #    if dest_number and re.search('^[\d\(\)\- \+]+$',dest_number):
     #       r.number(dest_number)
      #  else:
       #     r.client(dest_number)
    #return str(resp)


def wrong_number():
    from_number=request.values.get('From',None)
    resp=VoiceResponse()

    if from_number in callers:
        resp.say("Hello, "+callers[from_number])
        #resp.say("Enter the number you want to call, followed by pound.")
        #g = Gather(numDigits=11,finishOnKey='#', action="/handle-key", method="POST")
        g = Gather(finishOnKey='#', action="/handle-key", method="POST")
        g.say("Enter the number you want to call, followed by pound.")
        resp.append(g)

    else:
        resp.say("Wrong number.  You suck!")

    return str(resp)

@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():

    # Get the digit pressed by the user
    digits_pressed = request.values.get('Digits', None)
    resp = VoiceResponse()
    resp.say("Calling now, player.")   
    resp.dial(digits_pressed,callerId=caller_id)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=False)
