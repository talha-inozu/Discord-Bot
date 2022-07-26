
import discord
import os
from discord.ext import commands, tasks

intents = discord.Intents(messages = True, guilds = True , reactions = True, members = True, presences = True, message_content = True)
Bot = commands.Bot(command_prefix="!bot ", intents = intents)

@Bot.event
async def on_ready():
    # selamla.start()
    await Bot.change_presence(activity=discord.Activity(type = discord.ActivityType.listening,name = "!bot"))
    print("Ben hazırım")

@Bot.event
async def on_message(message):
    await Bot.process_commands(message)
    
    if message.channel ==  Bot.guilds[0].text_channels[6] and not message.author.bot and not message.content.startswith("!bot"):
        textString = message.content
        
        
        await message.channel.send(textString)
        
        
    # if not message.content.startswith("!bot"):
    #     await message.add_reaction("🤡")

@tasks.loop(seconds=5)  
async def selamla():
    await Bot.guilds[0].text_channels[0].send("Selam")

@Bot.command()
async def startSelam(ctx):
    selamla.start()
    
@Bot.command()
async def stopSelam(ctx):
    selamla.stop()


@Bot.command(aliases = ["gönder"])
async def send_message(msg, *args):
    string_A = " ".join(args) 
    await msg.send(string_A)



@Bot.command()
@commands.has_role("Executive")
async def move(msg, member: discord.Member, *,channel : discord.VoiceChannel):

    await member.move_to(channel)
    
    
    
@Bot.command()
@commands.has_role("Executive")
async def clear(ctx,amount = 10):    
    
    await ctx.channel.purge(limit= amount)



@Bot.command()
@commands.has_role("Executive")
async def channel_copy(ctx, name = "copiedchannel"):
    await ctx.channel.clone(name  = name)
    
    
    
@Bot.command()
@commands.has_role("Executive")
async def channel_del(ctx, channel : discord.TextChannel):
    await channel.delete()
    
    
    
@Bot.command()
@commands.has_role("Executive")
async def sendDM(ctx, member: discord.Member):
    await member.send(content="Selam")
    
    
    
@Bot.command()
@commands.has_role("Executive")
async def ban(ctx,member : discord.Member,*, reason = "Yok"):
    await member.ban(reason = reason)   
    await ctx.send(f"Banned user {member.mention} from {reason}")
    
    
@Bot.command()
@commands.has_role("Executive")
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discrimnator = member.split("#")
    
    for bans in banned_users:
        user = bans.user
        if(user.name,user.discriminator) == (member_name,member_discrimnator):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned user {user.mention}")
            break
    
    
    
@Bot.command()
@commands.has_role("Executive")
async def add_role(ctx,member:discord.Member,role:discord.Role):
    try:
        await member.add_roles(role,reason=None, atomic=True)
        await ctx.send(f"{member.mention} has given {role}")
    except Exception as e:
        error_message = str(e.args)
        if "Permissions" in error_message:
            await ctx.send("I haven't got Permission to do it!!")



@Bot.command()
@commands.has_role("Executive")
async def change_name(ctx,member:discord.Member,*args):
    nickname = " ".join(args)
    oldname = member.nick
    await member.edit(nick = nickname)
    await ctx.send(f"{oldname}'s new nickname is {member.mention}")
    
@Bot.command()
@commands.has_role("Executive")
async def load(ctx,extension):
    Bot.load_extension(f"cogs.{extension}") 
    await ctx.send(f"{extension} is loaded")
    
    
    
@Bot.command()
@commands.has_role("Executive")
async def unload(ctx,extension):
    Bot.unload_extension(f"cogs.{extension}") 
    await ctx.send(f"{extension} is unloaded")
    
@Bot.command()
@commands.has_role("Executive")
async def load_all(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            filename = filename[:-3]
            Bot.load_extension(f"cogs.{filename}")
    await ctx.send("All extenisons is loaded")        
            
@Bot.command()
@commands.has_role("Executive")
async def unload_all(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            filename = filename[:-3]
            Bot.unload_extension(f"cogs.{filename}")           
    await ctx.send("All extenisons is loaded")   
    
@Bot.command()
@commands.has_role("Executive")
async def update_extension(ctx,extension):
    try:
        Bot.unload_extension(f"cogs.{extension}") 
        Bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"{extension} is updated")
    except Exception as e:
        await ctx.send("This extension does not exist or not loaded yet !!")
    
Bot.run("OTk3NTEzNjc4Nzg0MDQwOTYx.G0EyFz.FWL7IfHnuLBwWpsJvayIKz30LZNmN1pfJ9qVYY")