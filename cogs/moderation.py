import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation commands loaded.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):

        # validity checks
        if (member == ctx.author):
            await ctx.send(f"Invalid argument; you cannot ban yourself.")
            return
        elif (member == self.client.user):
            await ctx.send(f"Invalid argument; you cannot ban me.")
            return

        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}.")

    @ban.error
    async def handleBanError(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument; must specify a member to ban.\n"
                            "Usage: !ban <member> (reason)")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument; member not found.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):

        if amount <= 0:
            await ctx.send("Invalid argument; amount must be greater than 0.")
        else: 
            await ctx.channel.purge(limit = amount + 1)
            await ctx.send(f"Deleted {amount} messages.")
    
    @clear.error
    async def handleClearError(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument; must specify the amount of messages to delete.\n"
                            "Usage: !clear <amount>")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument; amount must be an integer.")
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        # validity checks
        if (member == ctx.author):
            await ctx.send(f"Invalid argument; you cannot kick yourself.")
            return
        elif (member == self.client.user):
            await ctx.send(f"Invalid argument; you cannot kick me.")
            return

        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}.")

    @kick.error
    async def handleKickError(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument; must specify a member to kick.\n"
                            "Usage: !kick <member> (reason)")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument; member not found.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command.")


def setup(client):
    client.add_cog(Moderation(client))
