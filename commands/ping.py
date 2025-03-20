import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)

        embed = discord.Embed(
            title="Ping Response",
            color=discord.Color.blue() 
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        
        if latency < 100:
            embed.color = discord.Color.green()
            status = "Excellent"
        elif latency < 200:
            embed.color = discord.Color.gold()
            status = "Good"
        else:
            embed.color = discord.Color.red()
            status = "Poor"

        embed.description = f"Bot is responding with {status} latency."
        embed.add_field(name="Latency", value=f"{latency} ms", inline=True)
        embed.add_field(name="Status", value=status, inline=True)
        
        embed.set_footer(text="Ping Checked✅️")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))
