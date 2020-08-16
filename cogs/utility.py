import discord
from discord.ext import commands

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Utility commands loaded.")

    @commands.command()
    async def echo(self, ctx, *, args):
        await ctx.send(args)

    @echo.error
    async def handleEchoError(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument; must specify a message.\n"
                            "Usage: !echo <message>")

    @commands.command()
    async def latency(self, ctx):
        await ctx.send(f"Latency is {round(self.client.latency * 1000)} ms.")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):

        member = ctx.author if not member else member # member (default self)
        roles = [role for role in member.roles if not role.is_default()] # member roles
        member_created = member.created_at.strftime("%B %#d, %Y")
        member_joined = member.joined_at.strftime("%B %#d, %Y")

        embed = discord.Embed(
            color=member.color,
            timestamp=ctx.message.created_at
        )
        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Display Name", value=member.display_name)
        embed.add_field(name="Account Created", value=member_created)
        embed.add_field(name="Joined", value=member_joined)
        embed.add_field(name="Roles", value="".join([role.mention for role in roles] if roles else "None"))

        await ctx.send(embed=embed)

    @userinfo.error
    async def handleUserinfoError(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Missing argument; must specify a member.\n"
                            "Usage: !userinfo <member>")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid argument; member not found.")

def setup(client):
    client.add_cog(Utility(client))
