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
    elif what_do == "increment":
        increment_pokemon()
    elif what_do == "find":
        find_pokemon()
        main_menu(menu_count)
    elif what_do == "exit" or what_do == "quit" or what_do == "q":
        print("Quitting")
        exit()
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
    main_menu(1)

def print_pokemon(poke):
    print(f"{poke.id}: {poke.species} (\"{poke.name}\") - EVs: {poke.total_evs}")

def check_for_poke(poke):
    if poke == "EXIT":
        return False
    poke_list = Pokemon.select()
    poke_names = []
    for pokemon in poke_list:
        poke_names.append(pokemon.name)

    if poke in poke_names:
        return True
    return False

def find_pokemon():
    poke_name = input("Please enter pokemon name or type EXIT to go to main menu: ")
    check = check_for_poke(poke_name)
    if check == True:
        pokemon = Pokemon.get(Pokemon.name == poke_name)
        print("FOUND:")
        print_pokemon(pokemon)
        return pokemon
        
    elif poke_name != "EXIT":
        print("Error: pokemon does not exist")
        find_pokemon()
    else:
        print("returning to main menu")
        main_menu(1)
    

def increment_pokemon():
    pokemon = find_pokemon()
    continue_inc = True
    while continue_inc == True:
        incre_loop(pokemon)
        answer = input("Would you like to stop adding evs? (y/n) ").lower().strip()
        if answer == "y" or answer == "yes":
            continue_inc = False
    
    main_menu(1)
        
    
def incre_loop(pokemon):
    stat_increase = False
    while stat_increase == False and stat_increase != "EXIT":
        stat_increase = increase_stat(pokemon)


def increase_stat(pokemon):
    stat = input("What stat will you increase? (atk, defen, spe, spa, spd, hp) or type exit to leave ").lower().strip()
    amount = int(input("How many evs should be added? ").strip()) 
    if pokemon.total_evs + amount > 512:
        print("That exceeds the ev limit of 512")
        return "EXIT"
    elif stat == "atk": # pull keys and put them in a list and do an in conditional to shorten this
        print(f"adding {amount} evs to atk")
        pokemon.atk += amount
        pokemon.total_evs += amount
        pokemon.save()
        return amount
    elif stat == "defen":
        print(f"adding {amount} evs to defen")
        pokemon.defen += amount
        pokemon.total_evs += amount
        print(f"total evs: {pokemon.total_evs}")
        pokemon.save()
        return amount
    elif stat == "spe":
        print(f"adding {amount} evs to spe")
        pokemon.spe += amount
        pokemon.total_evs += amount
        print(f"total evs: {pokemon.total_evs}")
        pokemon.save()
        return amount
    elif stat == "spa":
        print(f"adding {amount} evs to spa")
        pokemon.spa += amount
        pokemon.total_evs += amount
        print(f"total evs: {pokemon.total_evs}")
        pokemon.save()
        return amount
    elif stat == "spd":
        print(f"adding {amount} evs to spd")
        pokemon.spd += amount
        pokemon.total_evs += amount
        print(f"total evs: {pokemon.total_evs}")
        pokemon.save()
        return amount
    elif stat == "hp":
        print(f"adding {amount} evs to hp")
        pokemon.hp += amount
        pokemon.total_evs += amount
        print(f"total evs: {pokemon.total_evs}")
        pokemon.save()
        return amount
    elif stat == "exit":
        print("exiting")
        return "EXIT"
    else:
        print(f"Error: {stat} is not a stat")
        return False

main_menu(0)