from typing import Text
from peewee import *
from werkzeug.datastructures import FileStorage

db = SqliteDatabase('officialData.db')


def init_db():
    db.connect()
    db.create_tables([BaseModel, User])
    print("Created the table....")


class BaseModel(Model):
    id = AutoField()

    class Meta:
        database = db


class User(BaseModel):
    login_id = CharField(unique=True)
    password = TextField()
    name = CharField()
    city = TextField()
    mobile = TextField()
    policeStation = CharField()
    rank = CharField()

    class Meta:
        pass


def saveData(received_name,  received_mobile, received_city, received_policeStation, received_rank, received_login_id, received_password):
    db.connect()
    try:
        print(received_rank)
        info = User(name=received_name, mobile=received_mobile,
                    city=received_city, policeStation=received_policeStation, rank=received_rank, login_id=received_login_id, password=received_password)
        info.save()
    except:
        print("error in saving data")
    db.close()


def retreiving_data(received_user_name):
    init_db()
    try:
        userInfo = User.select().where(
            User.login_id == received_user_name).get()
    except:
        return ""
    db.close()
    return userInfo.password
