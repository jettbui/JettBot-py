import discord
from discord.ext import commands

class Informational(commands.Cog):

    FOOTER = "JettBot by Jett Bui, © 2020"
    THUMBNAIL = 'https://cdn.discordapp.com/avatars/734847208154857493/30a1820b464b373e85a9a2f66233d7e4.png'
    INVITE = 'https://discord.com/api/oauth2/authorize?client_id=734847208154857493&permissions=8&scope=bot'

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Informational commands loaded.")

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(
            title="JettBot",
            description="A simple and straightforward Discord bot for your Discord server.",
            colour=discord.Colour.blue()
        )

        embed.set_thumbnail(
            url=Informational.THUMBNAIL)
        embed.add_field(name="Author", value="Jett Bui", inline=False)
        embed.add_field(name="Invite Link", value=Informational.INVITE, inline=False)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def help(self, ctx, category=None):
        author = ctx.message.author # user to send help message to

        if category == None:
            general_embed = discord.Embed(
                title="Commands",
                color=discord.Color.blurple()
            )
            general_embed.set_footer(text=Informational.FOOTER)
            general_embed.set_author(name="JettBot", icon_url=Informational.THUMBNAIL)
            general_embed.add_field(name="Customization", value="!help customization", inline=True)
            general_embed.add_field(name="Fun", value="!help fun", inline=True)
            general_embed.add_field(name="Informational", value="!help informational", inline=True)
            general_embed.add_field(name="Moderation", value="!help moderation", inline=True)
            general_embed.add_field(name="Utility", value="!help utility", inline=True)
            await author.send(embed=general_embed)
        elif category == "customization":
            customization_embed = discord.Embed(
                title="Customization Commands",
                color=discord.Color.blue()
            )
            customization_embed.set_footer(text=Informational.FOOTER)
            customization_embed.set_author(name="JettBot", icon_url=Informational.THUMBNAIL)
            customization_embed.add_field(name="!status <message>", value="Changes the status of the bot to the given argument", inline=True)
            await author.send(embed=customization_embed)
        elif category == "fun":
            fun_embed = discord.Embed(
                title="Fun Commands",
                color=discord.Color.magenta()
            )
            fun_embed.set_footer(text=Informational.FOOTER)
            fun_embed.set_author(name='JettBot', icon_url=Informational.THUMBNAIL)
            fun_embed.add_field(name="!8ball <question>", value="Ask the magic 8ball a question", inline=True)
            fun_embed.add_field(name="!flip", value="Flip a coin", inline=True)
            fun_embed.add_field(name="!roll", value="Roll a dice", inline=True)
            await author.send(embed=fun_embed)
        elif category == "informational":
            informational_embed = discord.Embed(
                title="Informational Commands",
                color=discord.Color.teal()
            )
            informational_embed.set_footer(text=Informational.FOOTER)
            informational_embed.set_author(name='JettBot', icon_url=Informational.THUMBNAIL)
            informational_embed.add_field(name="!about", value="Sends information about JettBot", inline=True)
            informational_embed.add_field(name="!help", value="Sends available commands for JettBot", inline=True)
            await author.send(embed=informational_embed)
        elif category == "moderation":
            moderation_embed = discord.Embed(
                title="Moderation Commands",
                color=discord.Color.green()
            )
            moderation_embed.set_footer(text=Informational.FOOTER)
            moderation_embed.set_author(name='JettBot', icon_url=Informational.THUMBNAIL)
            moderation_embed.add_field(name="!ban <user>", value="Ban a user from the server", inline=False)
            moderation_embed.add_field(name="Requires Permissions:", value="Ban Members", inline=False)
            moderation_embed.add_field(name="!clear <amount>", value="Clears a given number of messages in the current channel", inline=False)
            moderation_embed.add_field(name="Requires Permissions:", value="Manage Messages", inline=False)
            moderation_embed.add_field(name="!kick <user>", value="Kick a user from the server", inline=False)
            moderation_embed.add_field(name="Requires Permissions:", value="Kick Members", inline=False)
            await author.send(embed=moderation_embed)
        elif category == "utility":
            utility_embed = discord.Embed(
                title="Utility Commands",
                color=discord.Color.purple()
            )
            utility_embed.set_footer(text=Informational.FOOTER)
            utility_embed.set_author(name='JettBot', icon_url=Informational.THUMBNAIL)
            utility_embed.add_field(name="!echo <message>", value="Repeats message in the given argument", inline=True)
            utility_embed.add_field(name="!latency", value="Returns the latency of the bot", inline=True)
            utility_embed.add_field(name="!ping", value="Returns a ping message", inline=True)
            await author.send(embed=utility_embed)
        else:
            await author.send("Invalid argument, use '!help' for more info.")
    
    @commands.command()
    async def whomadeyou(self, ctx):
        if ctx.message.author.id == 80509831487692800:
            await ctx.send("You, <@80509831487692800>")
        else:
            await ctx.send(f"Not you, <@{ctx.message.author.id}>")

def setup(client):
    client.add_cog(Informational(client))
