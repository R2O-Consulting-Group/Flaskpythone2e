from flask import Flask,redirect,url_for
##WSGI Application 
app=Flask(__name__)

@app.route('/success/<int:score>')
def Pass(score):
    # return'Pass with ' + str(score)
    #try html formating 
    return'<html><body><h1> Pappu pass hogaya<h1></body></html>'
@app.route('/fail/<int:score>')
def Failegur(score):
    ## return'Fail with ' + str(score)
    #try html formating 
    return'<html><body><h1> Pappu Fail hogaya<h1></body></html>'

@app.route('/results/<int:marks>')
def results(marks):
    results=''
    if marks>=50:
        results = 'Pass'
    else:
        results = 'Failegur'
    return redirect (url_for(results,score=marks))


if __name__ =='__main__':
    app.run()