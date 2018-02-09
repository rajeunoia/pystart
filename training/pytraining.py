from chatterbot import ChatBot
import json
import sqlite3 as sq
from pymessenger.bot import Bot
from pymessenger import Element, Button


def write_questions_to_db(question, answer=""):
    conn = sq.connect("pw_unknown_question.db")
    if table_exists(conn,"questions"):
        conn.execute('insert into questions("question","answer") values ("'+question+'","'+answer+'")')
    else:
        conn.execute('create table  questions ("id" INTEGER PRIMARY KEY AUTOINCREMENT,"question" CHAR(100) NOT NULL,"answer" CHAR(100))')
        conn.execute('insert into questions("id","question","answer") values (1,"'+question+'","'+answer+'")')
    conn.commit()    
    conn.close()

#@app.route('/print_qsts',methods = ['POST', 'GET'])
def print_questions():
    conn = sq.connect("pw_unknown_question.db")
    qsts = ""
    if table_exists(conn,"questions"):
        result = conn.execute('select * from questions')
        qsts = result.fetchall()
        print(qsts)
    conn.close()
    return str(qsts)

#@app.route('/get_qsts',methods = ['GET'])
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
    return questions


def remove_question(id):
    conn = sq.connect("pw_unknown_question.db")
    qsts = ""
    questions = {}
    #id = request.args.get('id')   
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




