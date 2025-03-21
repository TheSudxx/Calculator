import discord
from discord import app_commands
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def create_help_embed(self):
        embed = discord.Embed(
            description="A powerful and easy to use Calculator bot designed for both simple and advanced Calculations, Currency Conversion, and more all within your server!",
            color=discord.Color.green()
        )

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else None)

        embed.add_field(
            name="• Configuration",
            value=f"My Prefix is {self.bot.command_prefix}",
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
            value="[Invite](https://discord.com/oauth2/authorize?client_id=833248024326963201&permissions=37080129&integration_type=0&scope=bot) | [Support Server](https://discord.com) | [Vote Me](https://top.gg/bot/833248024326963201/vote)",
            inline=False
        )

        embed.set_footer(
            text=f"Prefix: {self.bot.command_prefix} | Enjoy using {self.bot.user.name}",
            icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None
        )

        return embed

    @commands.command()
    async def help(self, ctx):
        embed = self.create_help_embed()
        await ctx.send(embed=embed)

    @app_commands.command(name="help", description="To show all commands")
    async def help_slash(self, interaction: discord.Interaction):
        embed = self.create_help_embed()
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
