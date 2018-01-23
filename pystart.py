# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import json
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


# Create a new chat bot named Pyson
@app.route('/support',methods = ['POST', 'GET'])
def support():
    chatbot = ChatBot(
        'Pyson',
        trainer='chatterbot.trainers.ListTrainer'
    )
    msg = "Hi"
    reply = ""
    response = chatbot.get_response(msg)
    if(response.confidence > 0.5 and msg.upper() != "BYE"):
        reply = response.serialize()
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
    response = chatbot.get_response(msg)
    if(response.confidence > 0.5 and msg.upper() != "BYE"):
        reply = response.serialize()
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