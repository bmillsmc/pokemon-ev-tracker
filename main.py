from peewee import *
from datetime import date

# run this with pipenv run python3 main.py or using python3 in the pipenv shell
# run settings.sql in the psql wiht \i settings.sql first to create the database (smh)

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


# - example code -

aegislash = Pokemon.create(name="firstaegislash", species="aegislash", atk=0, defen=0, spe=0, spa=0, spd=0, hp=0, total_evs=0)
# aegislash.save()
# print(f"{aegislash.id}: {aegislash.species} (\"{aegislash.name}\") - EVs: {aegislash.total_evs}")

# aegislash.total_evs += 2
# print(f"{aegislash.id}: {aegislash.species} (\"{aegislash.name}\") - EVs: {aegislash.total_evs}")


def main_menu(menu_count): # where the user starts. will take a user input and call the appropriate function
    if menu_count == 0:
        what_do = input("hello welcome to the pokemon ev tracker. what would you like to do? (list, create, increment, find) ").lower().strip()
    else: 
        what_do = input("what would you like to do? (list, create, increment, find, exit) ").lower().strip()
    menu_count += 1
    if what_do == "list":
        list_pokemon()
    elif what_do == "create":
        name = input("what is the pokemon's name? (NOT SPECIES this is a nickname) ")
        species = input("what is the pokemon's species? ")
        create_pokemon(name, species)
    # elif what_do == "increment":
    #     increment_pokemon()
    # elif what_do == "find":
    #     find_pokemon()
    elif what_do == "exit" or what_do == "quit" or what_do == "q":
        print("Quitting")
    else:
        print(f"Error: {what_do} is not a defined command. Please try again")
        main_menu(menu_count)

def list_pokemon():
    poke_list = Pokemon.select()
    for poke in poke_list:
        print_pokemon(poke)
    main_menu(1)

def create_pokemon(name, species, atk=0, defen=0, spe=0, spa=0, spd=0, hp=0, total_evs=0):
    pokemon = Pokemon.create(name=name, species=species, atk=atk, defen=defen, spe=spe, spa=spa, spd=spd, hp=hp, total_evs=total_evs)
    print("CREATED:")
    print_pokemon(pokemon)

def print_pokemon(poke):
    print(f"{poke.id}: {poke.species} (\"{poke.name}\") - EVs: {poke.total_evs}")

# def find_pokemon():

# def increment_pokemon():

main_menu(0)