import discord
from discord.ext import commands

# Create an instance of commands.Bot
bot = commands.Bot(command_prefix='!')

# Define a simple command
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

# Add the bot token to run the bot
bot.run('YOUR_BOT_TOKEN')
