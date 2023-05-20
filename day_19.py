from flask import Flask

app=Flask(__name__)

@app.route('/')

def sample():
    return 'kuch bhi sample'

@app.route('/new')
def sample1():
    return'<h1>This is Flask'

app.run(debug=True)



#google
#google.com
#https://www.google.com/
#https://www.google.com/search
#https://www.google.com/?='kuch bi hai'
