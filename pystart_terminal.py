# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import sqlite3 as sq
import json
# Create a new chat bot named Pyson

def support():
    chatbot = ChatBot(
        'Pyson',
        trainer='chatterbot.trainers.ListTrainer'
    )



    msg = ""
    # Get a response to the input text 'How are you?'
    while msg.upper() != "BYE":
        msg = input("You: ")
        response = chatbot.get_response(msg)
        if(response.confidence > 0.5 and msg.upper() != "BYE"):
            print(response)
        elif(msg.upper() != "BYE"):
            print("Sorry Didn't get you? Try these questiosn")
            sample_questions = ["Will i get a job after training?", "When is the next workshop?", "What is taught in 3 days workshop?"]
            print(sample_questions)
            write_questions_to_db(msg)
            
def write_questions_to_db(question, answer=""):
    conn = sq.connect("pw_unknown_question.db")
    if table_exists(conn,"questions"):
        conn.execute('insert into questions("question","answer") values ("'+question+'","'+answer+'")')
    else:
        conn.execute('create table  questions ("id" INTEGER PRIMARY KEY AUTOINCREMENT,"question" CHAR(100) NOT NULL,"answer" CHAR(100))')
        conn.execute('insert into questions("id","question","answer") values (1,"'+question+'","'+answer+'")')
    conn.commit()    
    conn.close()
    
def table_exists(conn,table_name):
    result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+table_name+"'")
    result_data = result.fetchall()
    if len(result_data)>0 and result_data[0][0] == table_name:
        return True
    else: 
        return False

support()
    
    