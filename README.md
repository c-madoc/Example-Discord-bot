# Basic Discord Bot

****

# Version: 0.1

A semi-advanced Discord bot including cogs, 
examples of database management, and basic command registration.

Highly commented for readability and understanding.


### Contains:

- Cogs with basic dynamic plugin loading
- Database connection to MongoDB with custom class structure 
- Custom Logger and Colors for terminal output
- Example test plugin with usage on interacting with the database cluster
- Settings class to easily manage the Discord bots settings

### Commands:
- `test`: Sends a basic Hello World
- `add_user`: Adds a user to the database
- `remove_user`: Removes a user from the database
- `users`: Gets all users from the database

### Setting up:
- Will need a `.env` file in the `src/` folder to store `TOKEN` and `DB`
- All requirements in `requirements.txt`