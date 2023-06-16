from flask import Flask,render_template,request,redirect
import nltk
from nltk.chat.util import Chat,reflections

################----ChatBot----################
#Rules for chat
rules=[
    #in form of tuple
    (r"hello",["hi","hello"]),
    (r"ac is not working",["pata nahi","humare yh asa hi hota h"])
]

my_chat_bot=Chat(rules)

#####################----Flask code----##################
app=Flask(__name__)#return the app name

@app.route('/')#decoraters:-connect this below function to above decorator to a web link
def home():
    return "Home page--"

@app.route('/chat',methods=['POST','GET'])
def chatbot():
    if request.method=='POST':
        ques=request.form['ask_mee']
        print(ques)
        res=my_chat_bot.respond(ques)
        print(res)
        return render_template("home.html",response_from_flask=res)
    else:
        return render_template("home.html")
app.run(debug=True)

#f"new string{res}"