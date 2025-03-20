import discord
from discord.ext import commands

class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def calc(self, ctx, num1: int, op: str, num2: int):
        embed = discord.Embed(
            title="Calculator Result",
            color=discord.Color.blue()
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)

        if op == "+":
            result = num1 + num2
            embed.description = f"{num1} + {num2} = {result}"
            embed.color = discord.Color.green()
        elif op == "-":
            result = num1 - num2
            embed.description = f"{num1} - {num2} = {result}"
            embed.color = discord.Color.green()
        elif op == "×" or op == "*":
            result = num1 * num2
            embed.description = f"{num1} {op} {num2} = {result}"
            embed.color = discord.Color.green()
        elif op == "÷" or op == "/":
            if num1 == 0:
                embed.description = "Hey, you can't divide by zero! Use your brain!"
                embed.color = discord.Color.red()
            elif num2 == 0:
                embed.description = "Hey, you can't divide by zero! Use your brain!"
                embed.color = discord.Color.red()
            else:
                result = num1 / num2
                embed.description = f"{num1} {op} {num2} = {result}"
                embed.color = discord.Color.green()
        else:
            embed.description = "Error: Invalid operator"
            embed.color = discord.Color.red()

        embed.add_field(name="Input", value=f"{num1} {op} {num2}", inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Calc(bot))
