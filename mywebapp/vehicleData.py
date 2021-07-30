from peewee import *

db = SqliteDatabase('vehicleDatabase.db')


def init_db():
    db.connect()
    db.create_tables([BaseModel, Vehicle])
    print("Created the table....")


class BaseModel(Model):
    id = AutoField()

    class Meta:
        database = db


class Vehicle(BaseModel):
    username = CharField()
    vehicleNumber = TextField()
    chassisNumber = TextField()
    engineNumber = TextField()

    class Meta:
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
