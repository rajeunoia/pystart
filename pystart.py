# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import json
import sqlite3 as sq
from pymessenger.bot import Bot
from flask import Flask, redirect, url_for, request
app = Flask(__name__)



#Get access token 
def get_access_token():
    token = "EAAbTWtBx3EEBAPICjzhEI3fuZB2BjvZBEpZArTq8XZAwnnFeI5BqFYPTT8TgJpaLEYOGs8L0NHE1ZALwZCoK4PnGyBCRl0ULBq9Ygw4IjCxZCneYNsV3kQLZApummj4y054rpTZCEySxLAZCuqHhymfMAqMzi9LqSMGxVRsfOLwExx1QZDZD"
    return token
    

client = Bot(get_access_token())  


def write_questions_to_db(question, answer=""):
    conn = sq.connect("pw_unknown_question.db")
    if table_exists(conn,"questions"):
        conn.execute('insert into questions("question","answer") values ("'+question+'","'+answer+'")')
    else:
        conn.execute('create table  questions ("id" INTEGER PRIMARY KEY AUTOINCREMENT,"question" CHAR(100) NOT NULL,"answer" CHAR(100))')
        conn.execute('insert into questions("id","question","answer") values (1,"'+question+'","'+answer+'")')
    conn.commit()    
    conn.close()

@app.route('/print_qsts',methods = ['POST', 'GET'])
def print_questions():
    conn = sq.connect("pw_unknown_question.db")
    qsts = ""
    if table_exists(conn,"questions"):
        result = conn.execute('select * from questions')
        qsts = result.fetchall()
        print(qsts)
    conn.close()
    return str(qsts)

@app.route('/get_qsts',methods = ['GET'])
def get_questions_json():
    conn = sq.connect("pw_unknown_question.db")
    qsts = ""
    questions = {}
    if table_exists(conn,"questions"):
        result = conn.execute('select * from questions')
        qsts = result.fetchall()
        for qst in qsts:
            if(qst[2] == ""):
                questions[qst[0]] = qst[1]
                
    conn.close()
    return json.dumps(questions)

@app.route('/remove_qst',methods = ['GET'])
def remove_question():
    conn = sq.connect("pw_unknown_question.db")
    qsts = ""
    questions = {}
    id = request.args.get('id')   
    if table_exists(conn,"questions"):
        result = conn.execute('delete from questions where id = '+id)
        conn.commit()        
    conn.close()
    return "ok",200  


def table_exists(conn,table_name):
    result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+table_name+"'")
    result_data = result.fetchall()
    if len(result_data)>0 and result_data[0][0] == table_name:
        return True
    else: 
        return False

    

#handle message
@app.route('/talk/<msg>',methods = ['POST', 'GET'])
def talk(msg="Hi"):
    chatbot = ChatBot(
        'Pyson',
        trainer='chatterbot.trainers.ListTrainer',
        read_only=True
    )
    #msg = "Hi"
    reply = ""
    resp = chatbot.get_response(msg)
    if(resp.confidence > 0.5 and msg.upper() != "BYE"):
        reply = resp.serialize()
        reply = reply["text"]
    elif(msg.upper() != "BYE"):
        reply = "Sorry Didn't get you? Try these questions "
        sample_questions = "Try: Will i get a job after training?  - "+ "When is the next workshop?   - " + "What is taught in 3 days workshop?"
        reply += sample_questions
        if reply not in msg:
            write_questions_to_db(msg)
    else:
        reply = "Thanks for talking to me, see you soon."
    return reply



#return response to messenger
def send_response(psid, response):
    #code to call graph api with response and token
    print(psid,response)
    client.send_text_message(psid,response)




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
        print("Input message - ",input_request_data)
        if input_request_data["object"] == "page":
            message_entries = input_request_data['entry']
            for entry in message_entries:
                for event in entry["messaging"]:
                    if "message" in event:
                        message = event["message"]
                        sender_id = event["sender"]["id"]
                        recipient_id = event["recipient"]["id"]
                        resp = talk(message["text"])
                        print("Output Response - ",resp)
                        send_response(sender_id, resp)
                    
                    
    return "ok",200    
 
# secure method to train the bot, this should not be exposed to external people
@app.route('/train',methods = ['GET'])
def train():
    if request.method == 'GET':
        question = request.args.get('question')    
        answer = request.args.get('answer')
        trainbot = ChatBot(
        'Pyson',
        trainer='chatterbot.trainers.ListTrainer')
        trainbot.train([question,answer])
    return "ok",200          


if __name__ == '__main__':
   app.run()




