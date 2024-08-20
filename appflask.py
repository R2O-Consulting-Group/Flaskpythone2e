
from flask import Flask
##WSGI Application 
app=Flask(__name__)


@app.route('/')
def welcome():
    return'Welcome to Choku flask'
@app.route('/newchok')
def welcome2():
    return'Welcome to Choku flask2'


if __name__ =='__main__':
    app.run()