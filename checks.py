import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

class NotOwner(commands.CheckFailure):
    ...

async def is_owner():
    async def predicate(ctx):
        if ctx.author.id != ctx.guild.owner_id:
            raise NotOwner("Hello! You are not the owner")
        return True
    return commands.check(predicate)

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command()
    @is_owner()
    async def say(ctx, what = "WHAT"):
        await ctx.send(what)

    async def say_error(ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("Permission denied.")

    bot.run(settings.TOKEN, root_logger=True)

if __name__ == "__main__":
    run()