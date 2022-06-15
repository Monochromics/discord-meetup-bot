#!/usr/bin/python3

# This example requires the 'message_content' privileged intent to function.
import discord
from discord.ext import commands
import scrape
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def events(ctx):
    await ctx.send(scrape.scrape())

bot.run(config['token'])
