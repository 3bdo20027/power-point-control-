import discord
from discord.ext import commands
import httpx 

Api_url= "http://127.0.0.1:8000" 


class Client(commands.Bot):

    async def on_ready(self):
        print(f'the Bot {self.user} run in your server') #print in terminal when bot run

        try:
            guild=discord.Object(id=1414237489358438493) #the bot run in spacific server

            synced= await self.tree.sync(guild=guild)
            print(f'synced {len(synced)} commands to guild {guild.id}')
        except Exception as ex:

            print(f'error is a {ex}')



intens=discord.Intents.all()

guild_id=1414237489358438493
guild=discord.Object(id=guild_id)

my_client=Client(case_insensitive=False,command_prefix='#',intents=intens)


#create power point buttons 

class view(discord.ui.View):
    @discord.ui.button(label='NEXT SLIDE',style=discord.ButtonStyle.gray,emoji='#️⃣')
    
    async def next_button(self,interaction:discord.Interaction,button:discord.ui.button):

        try:
            #send request to fast api
            async with httpx.AsyncClient() as client:
                
                await client.post(f'{Api_url}/ppt/next')
            
            await interaction.response.send_message('the next slide done',ephemeral=True)
        except Exception as ex:

            await interaction.response.send_message(f'Error {ex}',ephemeral=True)






@my_client.tree.command(name='pptx_conrol',description='this command cand cotrol for your presentaion by using buttons',guild=guild)

async def control(interactions:discord.Interaction):
    await interactions.response.send_message('the buttons displayed',view=view())


my_client.run('MTQxNjY1MDE3MjY2MTc2NDEwOA.G20Xuh.LhXqMFG5pGKGfSQ2LyfmYBwPH25EFtieJunbf0')





