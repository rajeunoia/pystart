# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import json
# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Pyson',
    trainer='chatterbot.trainers.ListTrainer'
)

general_conversation = [
    "Hi",
    "Hi, How can I help you",
    "Hello",
    "Hey, Do you have any questions about PythonWorkshops?", 
    "How are you",
    "I am good, How are you? Thanks for asking.",
    "Where are you",
    "Well i am everywhere, but for now infront of you.",
    "What is your name",
    "People like to call me Pyson",
    "Help",
    "I am here to help, Ask me questions about PythonWorkshops ?",
    "What can you do ?",
    "I am here to hep you about PythonWorkshops", 
    "I am good",
    "Good to know. shall we talk about PythonWorkshops", 
    "I am fine",
    "Good to know. shall we talk about PythonWorkshops",
    "Pyson",
    "Yes, How can i help you?", 
    "Thank you", 
    "No mention, its my pleasure talking to you", 
    "who are you?",
    "Pyson - Pythonworkshops support Team."
    
        
]

faqs_pystart = [
    "How to register for the workshops?",
    "Click on the link, www.pythonworkshops.com/register", 
    "Will i get a job after training?",
    "Our training exposes you to foundation of programming, which makes you job ready? but we can't assure a job",
    "When is the next workshop?",
    "check this link, www.pythonworkshops.com/#calendar",
    "What is taught in 3 days workshop?",
    "Check this link, www.pythonworkshops.com/3daysworkshop", 
    "what is python?",
    "well that is a good question, but quick answer, as we use english to communicate with each other, Python is a programming language, humans use to communicate with computers",
    "why do we program ?",
    "we program to automate human tasks", 
    "What is the workshop duration, how many days? ",
    "The combo workshop is 3 days, Intro to programming is 1 day, Python programming and Advanced Python is 2 days.",
    "What is pythonworkshops?",
    "Python workshops is our objective to spread programming across different communities, especially focused on python."
        
]

chatbot.train(general_conversation)
chatbot.train(faqs_pystart)

def learn_from_json(filename):
    faqs = []
    file_id = open(filename,'r')
    content = file_id.read()
    data = json.loads(content)

    for key in data.keys():
        print(data[key]['question'] +" -- "+ data[key]['answer'])
        faqs.append(data[key]['question'])
        faqs.append(data[key]['answer'])
    #print(faqs)
    chatbot.train(faqs)

'''
learn_from_json("./input/faqs_general.txt")
learn_from_json("./input/faqs_extending.txt")
learn_from_json("./input/faqs_gui.txt")
learn_from_json("./input/faqs_library.txt")
learn_from_json("./input/faqs_windows.txt")
learn_from_json("./input/faqs_programming.txt")
'''

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