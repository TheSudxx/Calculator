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
            name="• Configuration",
            value=f"My Prefix is !",
            inline=False
        )

        embed.add_field(
            name="• Commands [2]",
            value="calc, convert",
            inline=False
        )

        embed.add_field(
            name="• Utility [3]",
            value="ping, invite, alligator",
            inline=False
        )

        embed.add_field(
            name="• Links [3]",
            value="[Invite](https://discord.com) | [Support Server](https://discord.com) | [Vote](https://discord.com)",
            inline=False
        )

        embed.set_footer(
            text=f"Prefix: {self.bot.command_prefix} | Enjoy using {self.bot.user.name}",
            icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
