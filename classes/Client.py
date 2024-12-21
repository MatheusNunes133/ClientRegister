from peewee import *
from utils.load_env import *

psql_db = PostgresqlDatabase(database_name, user=username, password=password, host=host, port=port)

class BaseModel(Model):
    class Meta:
        database = psql_db

class Client(BaseModel):
    name = CharField()
    lastname = CharField()
    age = IntegerField()
    email = CharField()
    phone = CharField()