from flask import Flask, render_template, request, redirect
import nltk
from nltk.chat.util import Chat, reflections

#######################-------------- Chatbot code --------------------########################
# Rules for chat
rules = [
        # in the form of tuple
        (r"hello|hi",["hi", "hello"]),
        (r"ac is not working" ,["Pankha chalao", "hummare yaha aesa he hota h"]),
        (r"how are you",["I am Fine","How are you!!"]),
        (r"bye",["GoodBye","Nice to meet you"])
]

my_chat_bot = Chat(rules)

#######################-------------- Flask code --------------------########################

app = Flask(__name__)#return the app name

@app.route('/')#decoraters:-connect this below function to above decorator to a web link
def home():
    return "Home Page  ------"

@app.route('/chat', methods = ['POST', 'GET'])
def chatbot():
    # res = ""
    if request.method == "POST":
        ques = request.form['ask_me']
        print(ques)
        res = my_chat_bot.respond(ques)
        print(res)
        return render_template("home.html", response_from_flask = res)
    else:
        return render_template("home.html")

app.run(debug= True)