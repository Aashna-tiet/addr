from os import sendfile
from flask import request
from flask import session
from flask import render_template
from officialsData import *
from vehicleData import *
from flask import jsonify

# test functions


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

# for loggingninto a session


def login():
    error = ""
    if request.method == 'POST':
        if (request.form['username'] and request.form['password']):
            if valid_login(request.form['username'],
                           request.form['password']):
                session['username'] = request.form['username']
                user_name = request.form['username']
                return render_template('home.html', user=user_name, message="")
            else:
                error = "Oops!there might be a mistake in username or password that you entered!"
        else:
            error = 'please enter the details!'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('loginPage.html', error=error)

# for loggin out of the session


def logout():
    session.clear()
    return render_template('index.html', message="You are logged out now!")

# home page afer logging in


def home(user="Guest"):
    # return "Hi from home! Mr. "+str(session.get("username"))
    # return "Hi from home! Mr. "+str(user)
    return render_template("item.html", id=user)

# entry page of web app


def entry():
    msg = ""
    return render_template("index.html", message=msg)

# to do registrations


def doRegistration():
    error = ""
    if request.method == 'POST':
        if validRegistration(request.form['Name'], request.form['mobile'], request.form['city'], request.form['policeStation'], request.form['rank'], request.form['username'], request.form['password']):
            enterData(request.form['Name'], request.form['mobile'], request.form['city'],
                      request.form['policeStation'], request.form['rank'], request.form['username'], request.form['password'])
            message = "registration complete....please log in"
            return render_template('loginPage.html', error=message)
        else:
            error = "Please fill all the information required!"
    return render_template('registration.html', error=error)

# for validating registrations


def validRegistration(name,  mobile, city, policeStation, Rank, username, password):
    return name and mobile and city and policeStation and Rank and username and password

# for validation Vehicle registration


def validVehicleRegistration(name, vehicleNumber, chassisNumber, engineNumber):
    return name and vehicleNumber and chassisNumber and engineNumber

# for registering vehicle


def doVehicleRegistration():
    error = ""
    if request.method == 'POST':
        print(session['username'])
        if (validVehicleRegistration(session['username'], request.form['vehicleNumber'], request.form['chassisNumber'], request.form['engineNumber'])):
            enterVehicleData(session['username'], request.form['vehicleNumber'],
                             request.form['chassisNumber'], request.form['engineNumber'])
            error = "Done!"
            return render_template('home.html', user=session['username'], message="Done Vehicle registration!")
        else:
            error = "Sorry...Incomplete Fields!"
    return render_template('registerVehicle.html', error=error)

# saving vehicle data


def enterVehicleData(name, vehicleNumber, chassisNumber, engineNumber):
    saveVehicleData(name, vehicleNumber, chassisNumber, engineNumber)

# saving officers data


def enterData(name,  mobile, city, policeStation, Rank, username, password):
    saveData(name,  mobile, city, policeStation, Rank, username, password)

# retreiving data of vehicles


def vehicleData():
    array = retreiveData()
    x = len(array)
    print(x)
    if(x != 0):
        return render_template("item.html", vehicle=array)
    else:
        return render_template("item.html", error="Data Not Found!! Maybe an error occured!")


def trackLocations():
    if(request.method == "POST"):
        trackLocationOfVehicle(
            session['username'], request.form['vehicleNumber'], request.form['policeStation'])
        return render_template("home.html", user=session['username'])
    return render_template("location.html")


def searchVehicleDetails():
    if(request.method == "POST"):
        reg_vehicle = search(request.form['vehicleNumber'])
        locations = searchLocationDetails(request.form['vehicleNumber'])
        if(len(locations)):
            return render_template("particularVehicle.html", vehicle=reg_vehicle, location=locations, error="")
        else:
            return render_template("particularVehicle.html", error="Couldn't find any data.....Please check vehicle Number Again!")
    return render_template("searchVehicle.html")
