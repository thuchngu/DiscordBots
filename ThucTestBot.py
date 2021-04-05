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

@bot.command(name='yo', help='Responds with a greeting message')
async def yo(ctx):
    bot_messages = [
            'Hello Thuc!',
            'Hey there Thuc!',
            'Howdy partner!',
            (
                'The weather sure is nice today\n'
                'Wouldn\'t you say'
            ),
    ]
    response = random.choice(bot_messages)
    await ctx.send(response)

# TODO: incorporate a weather API to pull weather data and send as response
@bot.command(name='weather', help='Checks the weather for today')
async def weather(ctx):
    response = 'The weather today is'
    await ctx.send(response)

@bot.command(name='roll_dice', help='Simulates rolling dice')
async def roll(ctx, num_dice: int, num_sides: int):
    dice = [
            str(random.choice(range(1, num_sides + 1)))
            for _ in range(num_dice)
    ]
    await ctx.send(', '.join(dice))



@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)
#cust_client.run(TOKEN)
