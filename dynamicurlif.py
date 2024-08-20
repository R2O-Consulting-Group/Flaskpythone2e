##building dynamic url's if statement 

from flask import Flask
##WSGI Application 
app=Flask(__name__)


@app.route('/results/<int:score>')
def results(score):
    results=''
    if score>=50:
        results = ('Pass')
    else:
        results = ('Failegur')
    return results


if __name__ =='__main__':
    app.run()