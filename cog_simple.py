import discord
from discord.ext import commands
import settings
from cogs.greetings import Greetings

logger = settings.logging.getLogger("bot")


def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

        await bot.load_extension("cogs.greetings")

    bot.run(settings.TOKEN, root_logger=True)


if __name__ == "__main__":
    run()
