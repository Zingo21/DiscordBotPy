import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")


def run():
    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="!", intents=intents)

# TODO: add roles function

# TODO: add music funtion

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    bot.run(settings.TOKEN, root_logger=True)


if __name__ == "__main__":
    run()
