import discord
from discord.ext import commands

from helpers.database.models.user import Users
from helpers.database import connection as db
from helpers.tools.logger import Logger


class Test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.log = Logger(__name__)

    @staticmethod
    def add_user_to_database(user: discord.Member) -> [bool, str]:
        """ Adds a new user to the database. """

        # Check for the user in the database.
        user_db = Users().get(user.id)

        # If the user is in the database, return.
        if user_db:
            return False, f"{user} is already added in the database!"

        # Actually add the user to the database.
        added = Users().add(user.id, user.name, user.discriminator)

        # If the user was added to the database, return.
        if added:
            return True, f"Added {user} to the database."

        # If the user was not added to the database, return.
        return False, f"Failed to add {user} to the database."

    @staticmethod
    def remove_user_from_database(user: discord.Member) -> [bool, str]:
        """ Removes an existing user from the database. """

        # Check for the user in the database.
        user_db = Users().get(user.id)

        # If the user is in the database, return.
        if not user_db:
            return False, f"Could not find {user} in the database!"

        # Remove the user to the database.
        removed = db.remove(user_db)

        # If the user was removed from the database, return.
        if removed:
            return True, f"Removed {user} from the database."

        # If the user was not removed from the database, return.
        return False, f"Failed to remove {user} from the database."

    @staticmethod
    def get_users_from_database() -> str:
        """ Gets all users from the database. """

        # Get all users from the database.
        users = Users().get_all()

        # Return if there are no users in the database
        if len(users) == 0:
            return "There are no users in the database!"

        # Create a string, looping through all the users found.
        users_string = ""
        for user in users:
            users_string += f"- {user.name}#{user.discriminator}\n"

        return users_string

    @commands.command(aliases=["test"])
    async def test_command(self, ctx) -> None:
        """ A simple test command """
        await ctx.send("Hello world")

    @commands.command(aliases=["au", "add_user"])
    async def add_user_command(self, ctx, user: discord.Member) -> None:
        """ Adds a new user to the database, ignoring if they are already in there. """

        # Send an initial message stating what we are doing.
        msg = await ctx.send(f"Attempting to add {user.name}...")

        # Attempt to add the user to the database.
        added, message = self.add_user_to_database(user)

        # Edit the message we had sent to reflect the result.
        await msg.edit(content=message)

    @commands.command(aliases=["ru", "remove_user"])
    async def remove_user_command(self, ctx, user: discord.Member) -> None:
        """ Removes an existing user from the database. """

        # Send an initial message stating what we are doing.
        msg = await ctx.send(f"Attempting to remove {user.name}...")

        # Attempt to remove the user from the database.
        removed, message = self.remove_user_from_database(user)

        # Edit the message we had sent to reflect the result.
        await msg.edit(content=message)

    @commands.command(aliases=["gu", "get_users"])
    async def get_users_command(self, ctx) -> None:
        """ Gets all the users in the database. """

        # Send an initial message stating what we are doing.
        msg = await ctx.send(f"Attempting to get all users...")

        string = self.get_users_from_database()

        # Edit the message we had sent to reflect the result.
        await msg.edit(content=string)


def setup(bot) -> None:
    bot.add_cog(Test(bot))
