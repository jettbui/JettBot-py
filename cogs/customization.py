import discord
from discord.ext import commands

class Customization(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Customization commands loaded.")

    @commands.command()
    async def status(self, ctx, *, args):
        activity = discord.Game(name=args)
        await self.client.change_presence(status=discord.Status.online, activity=activity)
        await ctx.send(f"Status changed to '{args}'")

    @status.error
    async def handleStatusError(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument; must specify the status message to be set.\n"
                            "Usage: !status <message>")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument.")

def setup(client):
    client.add_cog(Customization(client))