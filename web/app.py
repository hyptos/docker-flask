import smtplib
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html', title='Home')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    strMessage 	= request.form['message']
    strName 	= request.form['name']
    strEmail 	= request.form['email']   
    s = smtplib.SMTP('localhost')
    s.sendmail("supermail@mailfai.com", strEmail, strMessage)
    s.quit()
    return "Your message has been sent !"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
