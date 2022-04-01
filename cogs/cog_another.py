from discord.ext import commands
from helpers.tools.logger import Logger


class Another(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.log = Logger(__name__)


def setup(bot) -> None:
    bot.add_cog(Another(bot))
