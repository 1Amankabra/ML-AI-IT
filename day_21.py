from flask import flask
app=flask(__name__)

@app.route('/')
def home():
    return 'Hi'

app.run(debug=True)