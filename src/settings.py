import os
from discord.ext import commands
import dotenv
from helpers.tools.logger import Logger

log = Logger(__name__)
dotenv.load_dotenv()


class Settings:
    name = "Test Bot"
    version = "0.1"
    version_name = "McTest"
    server = 'test'
    activity = "Testing"
    prefixes = ['.']
    guilds = []  # Guilds for potential slash command registration
    log_verbosity = Logger.Verbosity.debug  # Current values are low, default, high, and debug.

    token = os.environ.get("TOKEN")
    database = os.environ.get("DB")

    def get_prefix(self, ctx) -> list[str]:
        return Settings.prefixes
