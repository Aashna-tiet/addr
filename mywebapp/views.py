from os import sendfile
from flask import request
from flask import session
from flask import render_template
from loginData import *
from flask import jsonify


def test_ajax(msg, res_type):
    if res_type == 'json':
        return jsonify(message="Hello {0}".format(msg))
    else:
        return "Hello {0}".format(msg)


def myajax():
    return render_template("ajaxtest.html")


def valid_login(usernameProvided, passw):
    password = retreiving_data(usernameProvided)
    if(password):
        return password == passw
    else:
        return False


def login():
    error = ""
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            session['username'] = request.form['username']
            user_name = request.form['username']
            return render_template('home.html', user=user_name)
        else:
            error = 'Oops! Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('loginPage.html', error=error)


def logout():
    session.clear()
    return render_template('index.html', message="You are logged out now!")


def home(user="Guest"):
    # return "Hi from home! Mr. "+str(session.get("username"))
    # return "Hi from home! Mr. "+str(user)
    return render_template("item.html", id=user)


def entry():
    msg = ""
    return render_template("index.html", message=msg)


def doRegistration():
    error = None
    if request.method == 'POST':
        if validRegistration(request.form['Name'], request.form['age'], request.form['mobile'], request.form['city'], request.form['username'], request.form['password']):
            enterData(request.form['Name'], request.form['age'], request.form['mobile'],
                      request.form['city'], request.form['username'], request.form['password'])
            message = "registration complete....please log in"
            return render_template('loginPage.html', error=message)
        else:
            error = "Please fill all the information required!"
    return render_template('registration.html', error=error)


def validRegistration(name, age, mobile, city, username, password):
    return name and age and mobile and city and username and password


def enterData(name, age, mobile, city, username, password):
    saveData(name, age, mobile, city, username, password)
