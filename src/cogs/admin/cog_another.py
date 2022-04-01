import discord
from discord.ext import commands

from src.helpers.database.models.user import Users
from src.helpers.database import connection as db
from src.helpers.tools.logger import Logger


class Another(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.log = Logger(__name__)

def setup(bot) -> None:
    bot.add_cog(Another(bot))
