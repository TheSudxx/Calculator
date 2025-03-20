import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = os.getenv("API_KEY")  

    def get_exchange_rate(self, from_currency, to_currency):
        url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/{from_currency.upper()}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["result"] == "success":
                return data["conversion_rates"].get(to_currency.upper())
            else:
                return None
        return None

    @commands.command()
    async def convert(self, ctx, amount: float, from_currency: str, to_currency: str):
        embed = discord.Embed(
            title="Currency Conversion",
            color=discord.Color.blue() 
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)

        rate = self.get_exchange_rate(from_currency, to_currency)
        if rate:
            converted_amount = amount * rate
            embed.description = f"{amount} {from_currency.upper()} equals {converted_amount:.2f} {to_currency.upper()}."
            embed.add_field(name="Exchange Rate", value=f"1 {from_currency.upper()} = {rate} {to_currency.upper()}", inline=False)
            embed.color = discord.Color.green()  
        else:
            embed.description = "Error: Invalid currency code."
            embed.add_field(name="Tip", value="Please verify currency codes (e.g., USD, INR).", inline=False)
            embed.color = discord.Color.red()  

        embed.add_field(name="Input", value=f"{amount} {from_currency.upper()} to {to_currency.upper()}", inline=False)
        await ctx.send(embed=embed)

    @convert.error
    async def convert_error(self, ctx, error):
        embed = discord.Embed(
            title="Conversion Error",
            color=discord.Color.red()
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url if self.bot.user.avatar else None)

        if isinstance(error, commands.MissingRequiredArgument):
            embed.description = "Error: Incomplete command provided."
            embed.add_field(name="Correct Format", value=f"{self.bot.command_prefix}convert 100 USD INR", inline=False)
        elif isinstance(error, commands.BadArgument):
            embed.description = "Error: Amount must be a valid number."
            embed.add_field(name="Example", value=f"{self.bot.command_prefix}convert 100 USD INR", inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Currency(bot))
