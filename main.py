from flask import Flask , render_template,request
import requests
import smtplib

app=Flask(__name__)

email = 'your email is required here'             #you have to enter your email details .
password = "your password is required here"      #you have to enter your password .



@app.route('/')
def hello():
    req=requests.get('https://api.npoint.io/361fcf85637744a9d7e6')
    jso=req.json()
    return render_template('index.html',things=jso)

@app.route('/index.html')
def router():
    req = requests.get('https://api.npoint.io/361fcf85637744a9d7e6')
    jso = req.json()
    return render_template('index.html', things=jso)
@app.route('/about.html')
def abouter():
    return render_template('about.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/post.html/<int:value>')
def blogger(value):
    req=requests.get('https://api.npoint.io/361fcf85637744a9d7e6')
    jso=req.json()
    return render_template('post.html',numbers=jso,naam=value)

@app.route('/contact.html',methods=['POST'])
def receive_data():
    data = request.form
    # print(data["your_name"])                                              #smtplib — SMTP protocol client used here for sending the email messages
    # print(data["your_email"])
    # print(data["your_phone_number"])
    # print(data["your_email"])
    # return "<h1>Successfully sent your message</h1>"
    if request.method=='POST':
        the_name=request.form['your_name']
        the_phone_number=request.form['your_phone_number']
        the_mail=request.form['your_email']
        the_message=request.form['your_message']
        # zing=f'the name is {the_name} \n the mail is {the_mail} \n the phone_number is {the_phone_number} \n the mail is {the_mail} \n and the message is {the_message}'
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=email, password=password)
        #     connection.sendmail(email, "burnt1997@gmail.com",zing)    #here you have to mention the email adress of the person that you want to send the message
        #
        #     connection.close()

        print(f'the name is {the_name} \n the mail is {the_mail} \n the phone_number is {the_phone_number} \n the mail is {the_mail} \n and the message is {the_message}')

        # return (f'<h1>the name is {the_name} \n the mail is {the_mail} \n the phone_number is {the_phone_number} \n the mail is {the_mail} \n and the message is {the_message} </h1>')
        return render_template('contact-2.html',msg='successfully sent your message ')




























if __name__=="__main__":
    app.run(debug=True)
