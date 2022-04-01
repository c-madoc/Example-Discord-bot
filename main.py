import datetime
import os
import platform

import discord
from discord.ext import commands
from mongoengine import connect
from tabulate import tabulate

from helpers.tools.colors import Colors
from helpers.tools.logger import Logger
from helpers.tools.utils import SystemUtils
from settings import Settings


class Bot(commands.Bot):

    def __init__(self: "Bot"):
        super().__init__(command_prefix=Settings.get_prefix,
                         intents=discord.Intents.all())  # Set up the inherited bot class
        self.created = datetime.datetime.now()
        self.log = Logger(__name__)

    def load_plugins(self):
        """ Loads all plugins in the cogs folder. """
        file_prefix = "cog_"
        for root, dirs, files in os.walk("cogs"):
            for file in files:

                # If the file is a python file, try to load it as a cog
                if file.endswith(".py") and file.startswith(file_prefix):

                    # Set the file to include the root so we can find where the cog is when attempting to load
                    file = os.path.join(root, file)
                    plugin = {"name": "", "path": "", "split": []}

                    # If we are on a Windows system
                    if SystemUtils().get_system() == SystemUtils().windows:
                        plugin['split'] = file.split('\\')
                        plugin['name'] = plugin['split'][len(plugin['split']) - 1][len("cog_"):-3]
                        plugin['path'] = file.replace(f"cog_{plugin['name']}.py", "").replace("\\", ".")

                    # If we are on a Linux system
                    else:
                        plugin['split'] = file.split('/')
                        plugin['name'] = plugin['split'][len(plugin['split']) - 1][len(file_prefix):-3]
                        plugin['path'] = file.replace(f"{file_prefix}{plugin['name']}.py", "").replace("/", ".")

                    cog = f"{plugin['path']}{file_prefix}{plugin['name']}"

                    try:
                        # Actually load the cog
                        self.load_extension(cog)
                        self.log.success(f"{Colors.Foreground.green}Cog Loaded{Colors.reset}: {plugin['name']}")

                    except Exception as e:
                        if Settings.log_verbosity >= Logger.Verbosity.debug:
                            self.log.error(f"Plugin Failed to Load: {file}")

                # If there is a .py file but doesn't contain the file prefix, return a warning that it wasn't loaded
                elif file.endswith(".py") and not file.startswith(file_prefix):
                    if Settings.log_verbosity >= Logger.Verbosity.debug:
                        self.log.warning(f"{Colors.Foreground.yellow}Cog not Loaded{Colors.reset}: {file}")

    async def on_connect(self: "Bot") -> None:
        """ Fires when the Discord bot connects to the Discord servers. """
        self.log.info(f'The bot has connected to Discord.')

    async def on_ready(self: "Bot") -> None:
        """ Fires when the Discord bot is ready. """
        self.log.success(
            f'Successfully logged in as: {Colors.bold}{super().user}{Colors.reset} (id: {Colors.Foreground.orange}{super().user.id}{Colors.reset})')
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=Settings.activity))

    def print_greeting(self: "Bot") -> None:
        """ Prints a greeting on initialization. """
        info = [
            [f'⇢ {Colors.bold}Spawned{Colors.reset}', f'{Colors.Foreground.purple}{self.created}{Colors.reset}'],
            [f'⇢ {Colors.bold}Version{Colors.reset}',
             f'{Settings.name} ({Colors.Foreground.pink}v{Settings.version}{Colors.reset})[{Colors.Foreground.pink}{Settings.version_name}{Colors.reset}]'],
            [f'⇢ {Colors.bold}Library{Colors.reset}',
             f'Discord.py ({Colors.Foreground.pink}v{discord.__version__}{Colors.reset})'],
            [f'⇢ {Colors.bold}Platform{Colors.reset}',
             f'Python ({Colors.Foreground.pink}v{platform.python_version()}{Colors.reset})'],
            [f'⇢ {Colors.bold}System{Colors.reset}',
             f'{platform.system()} ({Colors.Foreground.pink}{platform.version()}{Colors.reset})']
        ]
        self.log.info(f'Attempting to start an instance of {Settings.name}...\n' + tabulate(info))

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
