from discord.ext import commands
import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
token = config.get("config", "token")
url = config.get("config", "url")
bot = config.get("config", "bot")


@bot.event
async def on_ready():
    print('Bot is online')


@bot.command(pass_context=True)
async def price(ctx, ticker):
    response = requests.get(url + ticker)
    fetched = response.json()
    symbol = fetched[0]['symbol']
    current_price = fetched[0]['current_price']
    formatted_price = '{0:,.4f}'.format(current_price)
    await ctx.send(symbol.upper() + '/USD: $' + str(formatted_price))


bot.run(token)
