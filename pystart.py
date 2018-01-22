# -*- coding: utf-8 -*-
from chatterbot import ChatBot
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