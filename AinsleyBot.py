import discord
import random
import time
from discord.ext import commands


bot = commands.Bot(command_prefix='zucc ')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def meme(ctx):
    meme = ["https://i.ytimg.com/vi/JTrArkG9Vyw/hqdefault.jpg"]
    embed = discord.Embed(title="Unfinished command shows pic of ainsley", color=0xeee657)
    embed.set_image(url=random.choice(meme))
    await ctx.send(embed = embed)


@bot.command()
async def sneaky(ctx):
    await ctx.send("I aM vERY snEakY Maiin")

@bot.command()
async def taco(ctx):
    await ctx.send("Adding Tacos")
    file = open("taco.txt", "r")
    tacos = file.read()
    file.close()
    await ctx.send("Read taco number")
    f = open('taco.txt', 'a')
    await ctx.send("33% done")
    newtaco = tacos + 1
    f.write("%s" % newtaco)
    await ctx.send("66% done")
    f.close()
    await ctx.send("Made tACoS, ver y sneakY BuSsiNEsS.")
    

@bot.command()
async def tacobusiness(ctx):
    embed = discord.Embed(title="Taco Business", color=0xeee657)
    embed.set_image(url=random.choice(meme))
    await ctx.send(embed = embed)

@bot.command()
async def hi(ctx):
    await ctx.send("Hello")


@bot.command()
async def iam(ctx, message):
    await ctx.send("wait")
    f = open('iamdata.txt', 'a')
    await ctx.send("33% done")
    f.write("Hello {0.author.mention \r\n".format(message))
    await ctx.send("66% done")
    f.close()
    await ctx.send("worked.")
    await ctx.send("Written member name in data base.")

@bot.command()
async def succ(ctx):
    await ctx.send(":eggplant:")
    
@bot.command()
async def thirsty(ctx):
    await ctx.send(":sweat_drops:")
    embed = discord.Embed(title="Oh damn im thirsty", color=0xeee657)
    embed.set_image(url="https://i.ytimg.com/vi/G5eywbcSeyU/maxresdefault.jpg")
    await ctx.send(embed = embed)
    await ctx.send(":sweat_drops:")
    
@bot.command()
async def die(ctx):
    await ctx.send("SYSTEM OVERLOAD, Self destruct in...")
    time.sleep(1)
    await ctx.send("3")
    time.sleep(1)
    await ctx.send("2")
    time.sleep(1)
    await ctx.send("1")
    embed = discord.Embed(title="Oof", color=0xeee657)
    embed.set_image(url="https://i.ytimg.com/vi/kAFh9zGMubM/hqdefault.jpg")
    await ctx.send(embed = embed)


@bot.command()
async def pic(ctx):
    await ctx.send("Don't ask for scale pics")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Spread Zucc", description="Lizard Bot", color=0xeee657)

    # give info about you here
    embed.add_field(name="ZuccDeveloper", value="NormieHater69")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Artificial Lizard Intelligence", value="Value of 1.")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Make Zucc Conquer The Web", value="Invite Link: https://discordapp.com/api/oauth2/authorize?client_id=439971633575362561&permissions=0&scope=bot")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Control The Zucc", description="List of commands are:", color=0xeee657)

    embed.add_field(name="Prefix", value="The prefix for every command is 'zucc' ", inline=False)
    embed.add_field(name="zucc meme", value="Shows a random meme about zucc", inline=False)
    embed.add_field(name="zucc joke", value="AMAZING! 10/10 joke! (Taken directly from quotes)", inline=False)
    embed.add_field(name="zucc hi", value="Hello", inline=False)
    embed.add_field(name="zucc info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="zucc help", value="Gives this message", inline=False)
    embed.add_field(name="zucc die", value="Self Destruct", inline=False)
    embed.add_field(name="zucc succ", value=":eggplant:", inline=False)

    await ctx.send(embed=embed)

bot.run('NDU2NjUyMDEwNDQwMzU5OTQ2.DgNp6g.kdB4_St9Ur-9Mb8XSbJ4x1W0Q6M')
