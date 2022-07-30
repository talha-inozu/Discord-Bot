import discord
from discord.ui import Select ,View
from discord.ext import commands
from random import randint
import os


class CommandSelect():
    
    
    def __init__(self,reponse,channel : discord.channel,text):
        self.response = reponse
        self.channel = channel
        self.commands = {
            "selamlama1":channel.send(self.response),
            "selamlasma":channel.send(self.response),
            "yaş1":channel.send(self.response)
        }
        self.text = text
        
    def getfunc(self):
        if  self.text in self.commands.keys():
            return self.commands.get(self.text)
        else:
            return self.channel.send("Bilinmeyen komut ya da tepki !")
    

    


class NLP(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
        
    @commands.Cog.listener()
    async def on_message(self,message):
        
    
        if message.channel ==  self.bot.guilds[0].text_channels[6] and not message.author.bot and not message.content.startswith("!bot"):
            textString = message.content
            response = randint(1,100)
            #response ve tag'i dictionary içindeki komutları editlemek için kullanıyorum
            command = CommandSelect(response,message.channel,textString)
            await command.getfunc()
            
            
            # await message.channel.send(textString)   
            
            


def setup(bot):
    bot.add_cog(NLP(bot))