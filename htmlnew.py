##integrate html wth flask 
## httpp verb GET and POST

from flask import Flask,redirect,url_for,render_template,request
##WSGI Application 

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index1.html')

@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    exp={'score':score,'res': res}
    return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def Failegur(score):
    return'Fail with ' + str(score)
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

##Result checket html submit page 
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    
    res=''
   
    return redirect(url_for('success',score=total_score))
if __name__ =='__main__':
    app.run()