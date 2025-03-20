import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.app_id = os.getenv("APP_ID")

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            description=f"Want to invite me to your server! [Click Here](https://discord.com/oauth2/authorize?client_id={self.app_id}&permissions=37080129&integration_type=0&scope=bot)",
            color=discord.Color.green()
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else None)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Invite(bot))
