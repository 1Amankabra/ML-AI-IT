from flask import Flask ,render_template
                           #app:-object
app=Flask(__name__)

@app.route('/')  #decorator
def sample():
    return 'kuch bhi sample'

@app.route('/new/<name>')
def sample1(name):
    print(name)
    return render_template('home.html',name_value=name)

app.run(debug=True)



#google
#google.com
#https://www.google.com/
#https://www.google.com/search
#https://www.google.com/?='kuch bi hai'
