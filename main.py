import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="!help | /help"))
    print(f"Your {bot.user} Is online")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} slash commands are sync!")
    except Exception as e:
        print(f"Slash commands sync problem: {e}")

async def load_extensions():
    await bot.load_extension("commands.calc")
    await bot.load_extension("commands.currency")
    await bot.load_extension("commands.ping")
    await bot.load_extension("commands.invite")
    await bot.load_extension("commands.alligator")   
    await bot.load_extension("commands.help")

@bot.event
async def setup_hook():
    await load_extensions()

if __name__ == "__main__":
    bot.run(TOKEN)
