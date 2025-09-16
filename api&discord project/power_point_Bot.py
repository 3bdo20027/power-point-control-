import discord
from discord.ext import commands
import httpx 
from get_path import pick_file
import asyncio
import sys
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
    
    async def on_member_join(self,member: discord.member):

        channel = discord.utils.get(member.guild.text_channels, name="general")  
        if channel:

            await channel.send(f'نورت السيرفر يحبيب اخوك  {member.mention} 🤖')



    




intens=discord.Intents.all()

guild_id=1414237489358438493
guild=discord.Object(id=guild_id)

my_client=Client(case_insensitive=False,command_prefix='#',intents=intens)





    
       


#create power point buttons 

class view(discord.ui.View):
   
   
   #create next button
    @discord.ui.button(label='NEXT SLIDE',style=discord.ButtonStyle.grey,emoji='⏩',row=1)
    
    async def next_button(self,interaction:discord.Interaction,button:discord.ui.button):

        try:
            #send request to fast api
            async with httpx.AsyncClient() as client:
                
                await client.post(f'{Api_url}/ppt/next')
            
            await interaction.response.send_message('the next slide done',ephemeral=True)
        except Exception as ex:

            await interaction.response.send_message(f'Error {ex}',ephemeral=True)
   

    #-------------------------------------------------------------------------------->

    #create pervious button
    @discord.ui.button(label='PREV SLIDE',style=discord.ButtonStyle.grey,emoji='⏪',row=1)
    
    async def prev_button(self,interaction:discord.Interaction,button:discord.ui.button):

        try:
            #send request to fast api
            async with httpx.AsyncClient() as client:
                
                await client.post(f'{Api_url}/ppt/prev')
            
            await interaction.response.send_message('the previous slide done',ephemeral=True)
        except Exception as ex:

            await interaction.response.send_message(f'Error {ex}',ephemeral=True)   
  
  #---------------------------------------------------------------------------->
  
   #cretae botton to open file
   
    @discord.ui.button(label='OPEN FILE',style=discord.ButtonStyle.danger,emoji="💻",row=0)

    async def open_ppt(self,interaction:discord.Interaction,button:discord.ui.button):
            await interaction.response.defer() #using for processes take alot time

            try:
                proc = await asyncio.create_subprocess_exec(
                    sys.executable #run by python
                    , "get_path.py"  #file will executable
                    ,
                    stdout=asyncio.subprocess.PIPE  #store any output from get_path.py as variablr
                    ,
                    stderr=asyncio.subprocess.PIPE  #store any error will output
                )

                stdout, stderr = await proc.communicate()   #get result of output or error
                file_path = stdout.decode().strip()  #convert file path as string

                if file_path:
                    json_data={"path" : file_path}

                    async with httpx.AsyncClient() as client:

                        try:
                            response=await client.post(f'{Api_url}/ppt/open',json=json_data)
                            if response.status_code == 200:
                               await interaction.followup.send("File path sent to FastAPI successfully!")
                            else:
                               await interaction.followup.send(f"Failed to send to FastAPI: {response.status_code}")
                        except Exception as e:
                           await interaction.followup.send(f"Error sending to FastAPI: {e}")

                else:
                    await interaction.followup.send('No file selected.')

            except Exception as e:
                await interaction.followup.send(f'Error: {e}')

    #---------------------------------------------------------------------------->
     
    #crete laser button

    @discord.ui.button(label='START LASER',style=discord.ButtonStyle.red,emoji='🔦',row=0)
    
    async def laser_button(self,interaction:discord.Interaction,button:discord.ui.button):

        try:
            #send request to fast api
            async with httpx.AsyncClient() as client:
                
                await client.post(f'{Api_url}/ppt/laser')
            
            await interaction.response.send_message('laser starts',ephemeral=True)
        except Exception as ex:

            await interaction.response.send_message(f'Error {ex}',ephemeral=True)
    #---------------------------------------------------------------------------->
     
    #crete stop button

    @discord.ui.button(label='STOP LASER || DRAWING || ERASE ',style=discord.ButtonStyle.blurple,emoji='❌',row=2)
    
    async def stop_button(self,interaction:discord.Interaction,button:discord.ui.button):

        try:
            #send request to fast api
            async with httpx.AsyncClient() as client:
                
                await client.post(f'{Api_url}/ppt/stop')
            
            await interaction.response.send_message('Stoped',ephemeral=True)
        except Exception as ex:

            await interaction.response.send_message(f'Error {ex}',ephemeral=True)
    
    #---------------------------------------------------------------------------->
     
    #crete draw button

    @discord.ui.button(label='START DRAW',style=discord.ButtonStyle.green,emoji='🖌',row=3)
    
    async def draw_button(self,interaction:discord.Interaction,button:discord.ui.button):

        try:
            #send request to fast api
            async with httpx.AsyncClient() as client:
                
                await client.post(f'{Api_url}/ppt/draw')
            
            await interaction.response.send_message('draw starts',ephemeral=True)
        except Exception as ex:

            await interaction.response.send_message(f'Error {ex}',ephemeral=True)
    #---------------------------------------------------------------------------->
     
    #crete erase button

    @discord.ui.button(label='START ERASE',style=discord.ButtonStyle.success,emoji='🗑',row=3)
    
    async def erase_button(self,interaction:discord.Interaction,button:discord.ui.button):

        try:
            #send request to fast api
            async with httpx.AsyncClient() as client:
                
                await client.post(f'{Api_url}/ppt/erase')
            
            await interaction.response.send_message('erase starts',ephemeral=True)
        except Exception as ex:

            await interaction.response.send_message(f'Error {ex}',ephemeral=True)








@my_client.tree.command(name='pptx_conrol',description='this command cand cotrol for your presentaion by using buttons',guild=guild)

async def control(interactions:discord.Interaction):
    await interactions.response.send_message('the buttons displayed',view=view())


my_client.run("MTQxNjY1MDE3MjY2MTc2NDEwOA.GfEQ0a.db8Dw0Oph4C-Kyq6x4j_EcdV7SD6cehIqbcN1k")





