from enum import unique
from flask.templating import render_template
from peewee import *
import datetime

from werkzeug.datastructures import FileStorage

db = SqliteDatabase('vehicleDatabase.db')


def init_db():
    db.connect()
    db.create_tables([BaseModel, Vehicle, Location])
    print("Created the table....")


class BaseModel(Model):
    id = AutoField()

    class Meta:
        database = db


class Vehicle(BaseModel):
    username = CharField()
    vehicleNumber = TextField(PrimaryKeyField)
    chassisNumber = TextField(unique)
    engineNumber = TextField(unique)

    class Meta:
        pass


class Location(BaseModel):
    policeStation = TextField()
    vehicleNumber = ForeignKeyField(Vehicle, backref='locations')
    date = DateTimeField()
    username = TextField()

    class meta:
        pass


def saveVehicleData(received_name, received_vehicleNumber, received_chassisNumber, received_engineNumber):
    db.connect()
    try:
        info = Vehicle(username=received_name,     vehicleNumber=received_vehicleNumber,
                       chassisNumber=received_chassisNumber, engineNumber=received_engineNumber)
        info.save()
    except:
        return "Error while saving vehicle Info"
    db.close()
    return ""


def trackLocationOfVehicle(received_name, received_vehicle_number, received_location):
    db.connect()
    try:
        info = Location(username=received_name,
                        vehicleNumber=received_vehicle_number, policeStation=received_location, date=datetime.datetime.now())
        info.save()
    except:
        return "Error while saving vehicle Info"
    db.close()
    return ""


def retreiveData():
    db.connect()
    array = []
    try:
        query = Vehicle.select()
        if(query):
            for vehicle in Vehicle.select():
                array.append(vehicle)
            # print(vehicle.vehicleNumber)
            print(array)
            return array
        else:
            errors = "No Vehicle found Sorry!"
            return render_template("item.html", error=errors)
    except:
        print("Error occured")
        return render_template("item.html", error="Error Occured!")


def search(received_vehicleNumber):
    db.connect()
    try:
        locations = []
        x = Vehicle.select().where(
            Vehicle.vehicleNumber == received_vehicleNumber).get()
        print(x)
        db.close()
        if(x):
            return x
        else:
            return ""
    except:
        db.close()
        return ""


def searchLocationDetails(received_vehicle_number):
    db.connect()
    try:
        locations = []
        y = Location.select().where(Location.vehicleNumber == received_vehicle_number)
        for i in y:
            locations.append(i)
        db.close()
        return locations
    except:
        db.close()
        return ""
