# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import json
# Create a new chat bot named Pyson

def support(msg):
    chatbot = ChatBot(
        'Pyson',
        trainer='chatterbot.trainers.ListTrainer'
    )

    reply = ""
    response = chatbot.get_response(msg)
    if(response.confidence > 0.5 and msg.upper() != "BYE"):
        reply = response.serialize()
    elif(msg.upper() != "BYE"):
        reply = "Sorry Didn't get you? Try these questions <br>"
        sample_questions = ["Will i get a job after training?", "When is the next workshop?", "What is taught in 3 days workshop?"]
        reply += sample_questions
    else:
        reply = "Thanks for talking to me, see you soon."
    return reply