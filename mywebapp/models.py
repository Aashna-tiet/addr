from peewee import *

db = SqliteDatabase('myapp.db')


def init_db():
    db.connect()
    db.create_tables([User, Pet])
    print("Created the tables.")


class BaseModel(Model):
    id = AutoField()

    class Meta:
        database = db


class User(BaseModel):
    login_id = CharField(unique=True, null=False)
    password_hashed = TextField(null=False)
    name = CharField(null=False)
    role = CharField()
    birthday = DateField()

    class Meta:
        pass


class Pet(BaseModel):
    pet_name = CharField()
    animalType = CharField()
    owner = ForeignKeyField(User, backref='pets')

    class Meta:
        pass
