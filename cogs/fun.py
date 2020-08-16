import discord
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun commands loaded.")

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, question):
        responses = ["For sure.",
                     "YEP",
                     "Probably.",
                     "I think so.",
                     "Maybe... maybe not.",
                     "I don't even know.",
                     "Probably not.",
                     "I don't think so.",
                     "NO."]
        await ctx.send(f"**Magic 8Ball**\nQuestion: _{question}_\n<:8ball:734976384782565447>: {random.choice(responses)}")
    
    @_8ball.error
    async def handle8BallError(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument; must specify a question.\n"
                            "Usage: !8ball <question>")

    @commands.command(aliases=["coin"])
    async def flip(self, ctx):
        responses = ["<:orange_circle:735583801249497138> Heads.",
                     "<:blue_circle:735725260321718302> Tails."]
        await ctx.send(f"**Flip a Coin**\n{random.choice(responses)}")

    @commands.command(aliases=["dice"])
    async def roll(self, ctx):
        responses = ["<:one:735714655934349385> Rolled a one.",
                     "<:two:735714655934349385> Rolled a two.",
                     "<:three:735714655934349385> Rolled a three.",
                     "<:four:735714655934349385> Rolled a four.",
                     "<:five:735714655934349385> Rolled a five.",
                     "<:six:735714655934349385> Rolled a six."]
        await ctx.send(f"**Roll the Dice**\n{random.choice(responses)}")

def setup(client):
    client.add_cog(Fun(client))