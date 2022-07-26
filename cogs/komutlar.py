
import discord
from discord.ui import Select ,View
from discord.ext import commands

class StatuSelect:  
    global statutext
    statutext = ""

    global globurl
    globurl = ""
    
    def __init__(self,text,url = ""):
        self.text = text     
        self.url = url
        global statutext
        statutext = text  #globalden kurtuluncak ve seçenekler eklenecek
        global globurl
        globurl = url
        self.myv = self.MyView()
        
    class MyView(View):
        
        @discord.ui.select(
                placeholder="Choose a statu !",
                options = [
                discord.SelectOption(label = "Playing",description = "!bot oynuyor",value="1"),
                discord.SelectOption(label = "Listening",description =  "!bot dinliyor",value="2"),
                discord.SelectOption(label = "Watching",description =  "!bot izliyor",value="3"),
                discord.SelectOption(label = "Streaming",description =  "!bot yayınlıyor",value="4")

            ])
        
        async def select_callback(self,select,interaction):
            select.disabled = True
            await interaction.response.edit_message(view = self)
            global statutext
            global globurl
            activities = {
            "1":{"activity":discord.Game(name=statutext)},
            "2":{"activity":discord.Activity(type=discord.ActivityType.listening ,name=statutext)},
            "3":{"activity":discord.Activity(type= discord.ActivityType.watching ,name=statutext)},
            "4":{"activity":discord.Streaming(name=statutext,url=globurl)}
             }
            await interaction.client.change_presence(**activities.get(str(select.values[0])))
                
        
class Komutlar(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.activities = {}
        
        
    @commands.command()
    async def merhaba(self,ctx):
        await ctx.send("Merhaba")
        

            
    @commands.command()
    async def change_status(self,ctx,url = "",*,text = ""):
        
        view = StatuSelect(text,url).myv

        await ctx.send("Choose !",view = view)
        

        
    
    



def setup(bot):
    bot.add_cog(Komutlar(bot))