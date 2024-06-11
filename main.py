import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")


def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

# TODO: add roles function

# TODO: add music funtion

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command(
        aliases=['p'],
        help="This is help",
        description="This is description",
        brief="This is brief"
    )
    async def ping(ctx):
        """ Answers with pong """
        await ctx.send("pong")

    bot.run(settings.TOKEN, root_logger=True)


if __name__ == "__main__":
    run()
