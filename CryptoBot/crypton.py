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

    @client.command(aliases=['CRYPTON', 'bot', 'crypto', 'hi', "Hi", "hello", "Hello", "price for "])
    async def crypton(ctx):
        await ctx.send(f'==========================================\n'
                       f'Welcome to Crypton! This is how bot works:\n'
                       f'----------------------------------------------\n'
                       f'For ONLY checking the prices:'
                       f'1. Write ".price ".\n'
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

    @client.command()
    async def what(ctx):
        await ctx.send(f"Select an option:\n"
                       f"https://www.forbes.com/sites/nextavenue/2021/06/18/cryptocurrency-101-all-you-really-need-to-know/?sh=3671df4d5b53\n"
                       f"https://medium.com/coinmonks/crypto-in-a-nutshell-for-beginners-cryptocurrency-101-in-2021-365c3e56fb84\n"
                       f"https://www.investopedia.com/terms/c/cryptocurrency.asp\n"
                       f"https://www.youtube.com/watch?v=Mvrq8hLjcRk")

    @client.command(aliases=['buy', 'Buy', "BUY", "Where"])
    async def where(ctx):
        await ctx.send(f"https://www.investopedia.com/best-crypto-exchanges-5071855\n"
                       f"https://www.coinbase.com/partner/Investopedia?clickId=3FY31P2LGxyIT0l2t-RrFXUXUkBXO5V5rSnm2A0&utm_source=impact&utm_medium=growthp&utm_campaign=rt_p_m_w_d_acq_imp_gro_aff_Dotdash&utm_content=1156380&utm_creative=Promo%20Code%20%2410%20BTC%20Investopedia&irgwc=1\n"
                       f"https://cash.app/\n"
                       f"https://bisq.network/")

    @client.command()
    async def region(ctx):
        await ctx.send(f"Canada: https://www.canada.ca/en/revenue-agency/programs/about-canada-revenue-agency-cra/compliance/digital-currency/cryptocurrency-guide.html\n"
                       f"China: http://www.gov.cn/xinwen/2021-05/21/content_5610192.htm\n"
                       f"USA: https://www.irs.gov/businesses/small-businesses-self-employed/virtual-currencies\n"
                       f"U.K: https://www.gov.uk/government/publications/tax-on-cryptoassets\n"
                       f"EU: https://www.oecd.org/tax/tax-policy/taxing-virtual-currencies-an-overview-of-tax-treatments-and-emerging-tax-policy-issues.pdf")

    #  Discord API Token
    client.run('ODk1ODQxNTYxOTQ5MTE4NTI0.YV-beA.76iZ_q91nNI2OoWSmefOniGUiUU')
