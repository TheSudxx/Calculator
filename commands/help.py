import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            description="A powerful and easy to use Calculator bot designed for both simple and advanced Calculations, Currency Conversion, and more all within your server!",
            color=discord.Color.green()
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else None)  

        embed.add_field(
            name=f"{self.bot.command_prefix}calc",
            value="Performs basic arithmetic operations (+, -, ×, ÷,).",
            inline=False
        )
        embed.add_field(
            name=f"{self.bot.command_prefix}convert",
            value="Converts an amount between different currencies.",
            inline=False
        )
        embed.add_field(
            name=f"{self.bot.command_prefix}ping",
            value="Displays the bot's current latency.",
            inline=False
        )
        embed.add_field(
            name=f"{self.bot.command_prefix}invite",
            value="Generates an invite link to add the bot to your server.",
            inline=False
        )
        embed.add_field(
            name=f"{self.bot.command_prefix}alligator",
            value="Shows bot information and links.",
            inline=False
        )

        avatar_url = self.bot.user.avatar.url if self.bot.user.avatar else None
        embed.set_footer(
            text=f"Prefix: {self.bot.command_prefix} | Enjoy using Alligator Bot",
            icon_url=avatar_url
        )
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
