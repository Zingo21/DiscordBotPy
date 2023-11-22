import settings
import discord
from discord.ext import commands


def run():
    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="!", intents=intents)

# TODO: add roles function

# TODO: add music funtion

    @bot.event()
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("_________________")

    bot.run(settings.TOKEN)


if __name__ == "__main__":
    run()