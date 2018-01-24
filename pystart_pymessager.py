# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import json
from pymessager.message import Messager
from flask import Flask, redirect, url_for, request
app = Flask(__name__)



#Get access token 
def get_access_token():
    token = "EAAbTWtBx3EEBAPICjzhEI3fuZB2BjvZBEpZArTq8XZAwnnFeI5BqFYPTT8TgJpaLEYOGs8L0NHE1ZALwZCoK4PnGyBCRl0ULBq9Ygw4IjCxZCneYNsV3kQLZApummj4y054rpTZCEySxLAZCuqHhymfMAqMzi9LqSMGxVRsfOLwExx1QZDZD"
    return token
    

client = Messager(get_access_token())   
    

#handle message
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



#return response to messenger
def send_response(psid, response):
    #code to call graph api with response and token
    print(psid,response)
    client.send_text(psid,response)




#Verify Token 
@app.route('/token',methods = ['POST', 'GET'])
def verify_token(verify_tkn):
    token = get_access_token()
    if(verify_token==token):
        return True
    else:
        return False


#handle postback
def handle_postback(psid,recieved_postback):
    
    return ""
    
    
# Create a new chat bot named Pyson
@app.route('/support',methods = ['POST', 'GET'])
def support():
    
    if request.method == 'GET':
        mode = request.args.get('hub.mode')    
        verify_tkn = request.args.get('hub.verify_token')    
        challenge = request.args.get('hub.challenge') 
        if mode=="subscribe" and verify_token(verify_tkn):
            return challenge
    if request.method == 'POST':
        #handle_post_events(request) - if required
        input_request_data = json.loads(request.data.decode('utf8'))
        print(input_request_data)
        if input_request_data["object"] == "page":
            message_entries = input_request_data['entry']
            for entry in message_entries:
                if "messaging" in entry[0]:
                    for event in entry["messaging"]:
                        if "message" in event:
                            message = event["message"]
                            sender_id = event["sender"]["id"]
                            recipient_id = event["recipient"]["id"]
                            resp = talk(message["text"])
                            print("Outside - ",resp)
                            if "text" in resp:
                                print("Inside - ",resp)
                                send_response(recipient_id, resp)
                    
                    
    return "ok",200    
 



if __name__ == '__main__':
   app.run()




