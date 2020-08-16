import discord
import os
import sys
import traceback
import logging
from discord.ext import commands

TOKEN = '<your token here>' # bot token

# for logging
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

# load all cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    activity = discord.Game(name="Use !help for commands")
    await bot.change_presence(status=discord.Status.online, activity=activity)

    print(f"Logged in as {bot.user.name}.")

@bot.event
async def on_member_join(ctx):
    await ctx.send("Hello!")

@bot.event
async def on_message(message):
    author = message.author
    content = message.content
    channel = message.channel

    if message.content.lower() == "jett":
        await channel.send("Sup")

    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel

    print(f"Message deleted from '{author}': '{content}'")

@bot.event
async def on_command_error(ctx, error):

    # catch errors handled locally
    if hasattr(ctx.command, 'on_error'):
        return

    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found, use '!help' for more info.")
    else:
        print(f"Ignoring exception in command {ctx.command}:", file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

@bot.command(no_pm=True)
async def reload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.unload_extension(f'cogs.{filename[:-3]}')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
    await ctx.send("JettBot has been reloaded.")
    print("JettBot reloaded.")
    
bot.run(TOKEN)
