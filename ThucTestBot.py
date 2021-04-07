# ThucTestBot.py

import os
import discord
import random
import python_weather
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

w_client = python_weather.Client(format=python_weather.IMPERIAL)
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
@bot.command(name='weather_today', help='Checks the weather for today')
async def weather_today(ctx):
    weather = await w_client.find("Washington DC")
    response = 'The weather today is' + weather.current
    await ctx.send(response)

@bot.command(name='weather_forecast', help='Checks the weather forecast for the next few days')
async def weather_forecast(ctx):
    weather = await w_client.find("Washington DC")
    for forecast in weather.forecast:
        await ctx.send(str(forecast.date), forecast.sky_text, forecast.temperature)

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
await w_client.close()
