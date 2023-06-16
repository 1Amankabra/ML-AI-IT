import nltk
from nltk.chat.util import Chat,reflections

#Rules for chat
rules=[
    #in form of tuple
    (r"hello",["hi","hello"]),
    (r"ac is not working",["pata nahi","humare yh asa hi hota h"])
]

my_chat_bot=Chat(rules)

res=my_chat_bot.respond("hello")
print(res)