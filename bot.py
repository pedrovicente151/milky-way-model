from random import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot online.")

@client.command()
async def regular_call(ctx):
    await ctx.send(f"Pong!")

@client.command(aliases=['bot', 'test'])
async def question(ctx, *, question):
    await ctx.send(f"Question: {question}\nAnswer:{question}")

client.run('ODk1ODQxNTYxOTQ5MTE4NTI0.YV-beA.Jtvgp-hsb_H9Wudt0j16SUe-cIg')
