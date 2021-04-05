# ThucTestBot.py

import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='yo')
async def yo(ctx):
    bot_messages = [
            'Hello Thuc!',
            'Hey there Thuc!',
            'Howdy partner!',
            (
                'The weather sure is nice today'
                'Wouldn\'t you say'
            ),
    ]
    response = random.choice(bot_messages)
    await ctx.send(response)

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)
#cust_client.run(TOKEN)
