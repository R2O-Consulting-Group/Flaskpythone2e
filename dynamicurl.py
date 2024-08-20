##building dynamic url's 

from flask import Flask
##WSGI Application 
app=Flask(__name__)


@app.route('/')
def welcome():
    return'Welcome to Choku flask'

@app.route('/success/<int:score>')
def success(score):
    return'Pass with ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return'Fail with ' + str(score)

if __name__ =='__main__':
    app.run()