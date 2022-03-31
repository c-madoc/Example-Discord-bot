import datetime
import os

import discord
from discord.ext import commands
from mongoengine import connect
from helpers.tools.colors import Colors
from helpers.tools.logger import Logger
from settings import Settings


class Bot(commands.Bot):

    def __init__(self: "Bot"):
        super().__init__(command_prefix=Settings.get_prefix,
                         intents=discord.Intents.all())  # Set up the inherited bot class
        self.created = datetime.datetime.now()
        self.log = Logger(__name__)

    def load_plugins(self):
        """ Loads all plugins in the cogs folder. """
        for root, dirs, files in os.walk("cogs"):
            for file in files:

                # If the file is a python file, try to load it as a cog
                if file.endswith(".py"):
                    try:
                        self.load_extension(f"cogs.{file.replace('.py', '')}")
                        self.log.success(f"Loaded {file}")
                    except Exception as e:
                        self.log.error(f"Error: {e}")

    async def on_connect(self: "Bot") -> None:
        """ Fires when the Discord bot connects to the Discord servers. """
        self.log.info(f'The bot has connected to Discord.')

    async def on_ready(self: "Bot") -> None:
        """ Fires when the Discord bot is ready. """
        self.log.success(
            f'Successfully logged in as: {Colors.bold}{super().user}{Colors.reset} (id: {Colors.Foreground.orange}{super().user.id}{Colors.reset})')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=Settings.activity))

    def print_greeting(self: "Bot") -> None:
        """ Prints a greeting. """
        self.log.info(f'Attempting to start an instance of {Settings.name}...')

    def start_bot(self: "Bot") -> None:
        """ Connects the bot to a MongoDB cluster, loads all the plugins, and starts the bot. """
        connect(Settings.server, host=Settings.database)  # Connect to MongoDB
        self.load_plugins()  # Load all plugins in the cogs folder
        super().remove_command('help')  # Remove the basic help docs
        super().run(Settings.token, bot=True, reconnect=True)  # Start the bot with the provided token


def main() -> None:
    bot = Bot()
    bot.print_greeting()
    bot.start_bot()


if __name__ == "__main__":
    main()
