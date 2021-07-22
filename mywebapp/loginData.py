from peewee import *

db = SqliteDatabase('data.db')


def init_db():
    db.connect()
    db.create_tables([User])
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
    age = CharField()

    class Meta:
        pass


def saveData(received_name, received_age, received_mobile, received_city, received_login_id, received_password):
    db.connect()
    u = User(login_id=received_login_id, password=received_password,
             name=received_name, city=received_city, mobile=received_mobile, age=received_age)
    u.save()
    db.close()


def retreiving_data(received_user_name):
    init_db()
    userInfo = User.select().where(User.login_id == received_user_name).get()
    return userInfo.password
