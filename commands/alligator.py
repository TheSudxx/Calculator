import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

class Alligator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.app_id = os.getenv("APP_ID")

    @commands.command()
    async def alligator(self, ctx):
        embed = discord.Embed(
            description="Alligator is a versatile bot designed to assist with calculations, currency conversion, and more!",
            color=discord.Color.green()
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)

        invite_link = f"https://discord.com/oauth2/authorize?client_id={self.app_id}&permissions=37080129&integration_type=0&scope=bot"
        embed.add_field(
            name="Want to invite me to your server",
            value=f"[Click Here]({invite_link})",
            inline=False
        )

        support_link = "https://discord.gg/YOUR_SUPPORT_SERVER_INVITE"
        embed.add_field(
            name="Need support or encountered a bug",
            value=f"Join my server: [Click Here]({support_link})",
            inline=False
        )

        topgg_link = "https://top.gg/bot/833248024326963201/vote"
        embed.add_field(
            name="Enjoying using Alligator",
            value=f"You can support us by voting on [Top.gg]({topgg_link})",
            inline=False
        )

        await ctx.send(embed=embed)

    @alligator.error
    async def alligator_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            embed = discord.Embed(
                title="Access Denied",
                description="This command is restricted to the bot owner only.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Alligator(bot))
