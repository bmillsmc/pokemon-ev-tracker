from peewee import *
from datetime import date
# run this with pipenv run python3 main.py or using python3 in the pipenv shell

db = PostgresqlDatabase("pokemon", user="postgres", password="", host="localhost", port="5432")

class BaseModel(Model):
    class Meta:
        database = db

class Pokemon(BaseModel):
    name = TextField(unique=True) # identifier for pokemon, for example, kingsshieldaegislash
    species = TextField() # pokemon species, for example, aegislash
    atk = IntegerField() # attack ev stat
    defen = IntegerField() # defense ev stat
    spe = IntegerField() # speed ev stat
    spa = IntegerField() # special attack ev stat
    spd = IntegerField() # special defense ev stat
    hp = IntegerField() # health points ev stat
    total_evs = IntegerField() # how many evs the pokemon has gained, shouldn't exceed 512

db.connect()
db.drop_tables([Pokemon])
db.create_tables([Pokemon])

aegislash = Pokemon(name="firstaegislash", species="aegislash", atk=0, defen=0, spe=0, spa=0, spd=0, hp=0, total_evs=0)
aegislash.save()
print(f"{aegislash.id}: {aegislash.species} (\"{aegislash.name}\") - EVs: {aegislash.total_evs}")
