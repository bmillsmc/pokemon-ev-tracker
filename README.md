# Pokemon EV Tracker

Using the command line you can track your Pokemons' EVs while training them for competitive play

## Technologies Used

The languages and libraries utilized in this project are:

- Python 3
- PeeWee
-

## Getting Started

### Installation

1. Clone down the repo into a folder using `git clone [SSH KEY]`
2. Install dependencies using `pipenv install`
3. Run the `settings.sql` to set up the database, using the command `psql -U postgres -f settings.sql`
4. Launch the application from the root of the directory using `pipenv run python main.py`
5. Follow on screen prompts or go to the Usage section

## Usage

Upon launching the command line you will be prompted with what you would like to do. This has 5 commands:

- List
- Create
- Find
- Increment
- Quit

These commands are not case sensitive. All commands, once done, will return to the main menu.

### List

Once entered the `List` command will list out the Pokemon currently contained in your database. It is recommended to use the `List` command first when the program is started as it will show you what your database contains and you can move from there.

### Create

This command allows the creation of a new Pokemon starting at 0 EVs for all stats. All thats required are:

- Name (a unique identifier)
- Species (what Pokemon it is i.e. Pikachu)

Once run the command will give you the output of the new Pokemon.

### Find

This command accepts a Pokemon's name, finds it in the database and returns it.

### Increment

This is the bread and butter of the application. This command allows you to add stats to any of the 6 stat fields:

- Attack (atk)
- Defense (defen)
- Speed(spe)
- Special Defense(spd)
- Special Attack(spa)
- Health Points(hp)

After entering a field you will be prompted to enter the amount of points that it improved by. A Pokemon's EVs cannot exceed 512 and the program reflects this as it will not add to a total of more than 512.

### Quit

Also accepts `Exit`, the quit command quits the application.

## Suggestions

I'm always looking to learn and grow as a developer. I'm not afraid of critisism, so please don't be afraid to give me suggestions for the site to make it better. Also please always point out bugs so that I can fix them.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Planned Updates

- Adding the ability to delete Pokemon
- Adding the ability to subtract evs
- Adding the ability to save outside of the program NOTE: CURRENTLY THE PROGRAM WILL NOT SAVE ANY CHANGES MADE BEFORE IT CLOSES
