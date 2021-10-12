import requests
from requests import Session
import secrets
from pprint import pprint
from random import random
import discord
from discord.ext import commands

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/map"

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': "078f23d5-6746-4863-b078-3cd159a7a6c5",
}


class CMC:

    def __init__(self, token):
        self.apiurl = "https://pro-api.coinmarketcap.com"
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
        self.session = Session()
        self.session.headers.update(self.headers)

    def get_ten_coins(self):
        """Return the top 10 cryptos.
        """
        url = self.apiurl + "/v1/cryptocurrency/listings/latest"
        r = self.session.get(url)
        data = r.json()['data'][:10]  # Set crypto limit.
        return data

    def get_names(self):
        url = self.apiurl + "/v1/cryptocurrency/map"
        r = self.session.get(url)
        data = r.json()['data'][:10]

        return data


class DiscordBot:
    client = commands.Bot(command_prefix='.')

    cmc = CMC("078f23d5-6746-4863-b078-3cd159a7a6c5")
    all_coins = cmc.get_ten_coins()

    pprint(all_coins)

    @client.event
    async def on_ready():
        print("Crypton online.")

    @client.command(aliases=['CRYPTON', 'bot', 'crypto', 'hi', "Hi", "hello", "Hello"])
    async def crypton(ctx):
        await ctx.send(f'==========================================\n'
                       f'Welcome to Crypton! This is how bot works:\n'
                       f'----------------------------------------------\n'
                       f'1. Select a discord dot command (below).\n'
                       f"2. Use the crypto's name.\n"
                       f"3. Use a question mark after crypto's name\n"
                       f'Example: .price dogecoin?\n'
                       f'==========================================\n'
                       f'Select a command:\n'
                       f"A).price - Check Crypto's price.\n"
                       f'B).what - Learn about currency.\n'
                       f'C).where - Where to buy crypto.\n'
                       f"D).region - Check Crypto's location availability.")

    @client.command(aliases=['value', 'PRICE'])
    async def price(ctx, *, question):
        """Returns requested crypto price on Discord
        """

        cmc = CMC("078f23d5-6746-4863-b078-3cd159a7a6c5")
        all_coins = cmc.get_ten_coins()

        crypto_name = str(question).lower()[:-1].capitalize()

        for coin in all_coins:
            if coin['name'] == crypto_name:
                crypto_price = coin['quote']['USD']['price']

                await ctx.send(f"Question: {question}\nAnswer:{round(crypto_price, 4)}")
                await ctx.send(f"What next?: \n"
                               f"A).price - Check Crypto's price.\n"
                               f'B).what - Learn about currency.\n'
                               f'C).where - Where to buy crypto.\n'
                               f"D).region - Check Crypto's location availability.")

    #  Discord API Token
    client.run('ODk1ODQxNTYxOTQ5MTE4NTI0.YV-beA.cleyX6AhHwsaNic54SPRHWy6yj0')
