# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import json
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


# Create a new chat bot named Pyson
@app.route('/support',methods = ['POST', 'GET'])
def support():
    token = "EAAbTWtBx3EEBAPICjzhEI3fuZB2BjvZBEpZArTq8XZAwnnFeI5BqFYPTT8TgJpaLEYOGs8L0NHE1ZALwZCoK4PnGyBCRl0ULBq9Ygw4IjCxZCneYNsV3kQLZApummj4y054rpTZCEySxLAZCuqHhymfMAqMzi9LqSMGxVRsfOLwExx1QZDZD"
    if request.method == 'GET':
        mode = request.args.get('hub.mode')    
        verify_token = request.args.get('hub.verify_token')    
        challenge = request.args.get('hub.challenge') 
    if mode=="subscribe" and token == verify_token:
        return challenge
    chatbot = ChatBot(
        'Pyson',
        trainer='chatterbot.trainers.ListTrainer'
    )
    msg = "Hi"
    reply = ""
    resp = chatbot.get_response(msg)
    if(resp.confidence > 0.5 and msg.upper() != "BYE"):
        reply = resp.serialize()
    elif(msg.upper() != "BYE"):
        reply = "Sorry Didn't get you? Try these questions <br>"
        sample_questions = "Will i get a job after training?   "+ "When is the next workshop?  " +  "What is taught in 3 days workshop?"
        reply += sample_questions
    else:
        reply = "Thanks for talking to me, see you soon."
    return json.dumps(reply)



@app.route('/talk/<msg>',methods = ['POST', 'GET'])
def talk(msg="Hi"):
    chatbot = ChatBot(
        'Pyson',
        trainer='chatterbot.trainers.ListTrainer'
    )
    #msg = "Hi"
    reply = ""
    resp = chatbot.get_response(msg)
    if(resp.confidence > 0.5 and msg.upper() != "BYE"):
        reply = resp.serialize()
    elif(msg.upper() != "BYE"):
        reply = "Sorry Didn't get you? Try these questions <br>"
        sample_questions = "Will i get a job after training?  - "+ "When is the next workshop?   - " + "What is taught in 3 days workshop?"
        reply += sample_questions
    else:
        reply = "Thanks for talking to me, see you soon."
    return json.dumps(reply)

@app.route('/token',methods = ['POST', 'GET'])
def token():
    return ""
if __name__ == '__main__':
   app.run()