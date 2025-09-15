import discord
from discord.ext import commands
from discord import app_commands



class Client(commands.Bot):
    #when bot run
    async def on_ready(self):
        print(f'Congrats your bot is run {self.user}')


        try:
            guild=discord.Object(id=1414237489358438493)

            synced=await self.tree.sync(guild=guild)

            print(f'synced {len(synced)} commands to guild {guild.id}')
        except Exception as ex:

            print(f'error is a {ex}')

    #when message send
    async def on_message(self,message):

        print(f'the member {message.author} send : {message.content}')
        print(f'Message from {message.author} : {message.content}')

        if message.author==self.user:
            return
        
        if message.content.startswith('hi'):
            await message.channel.send(f'HI there {message.author}')








#this code run on spacific server

guild_id=discord.Object(id=1414237489358438493)

intens=discord.Intents.default()
intens.message_content=True


client=Client(command_prefix='!',intents=intens)




#now ley's create a command

@client.tree.command(name='say_hellow',description='this say hellow for member',guild=guild_id)

async def sayhi(interactions : discord.Interaction):

    await interactions.response.send_message('hi bro how are you')


@client.tree.command(name='new',description='new command ',guild=guild_id)

async def new_command(interactions :discord.Interaction,printer :str):
    await interactions.response.send_message(printer)




#now let's craete a button

class view(discord.ui.View):

    @discord.ui.button(label='smile face',style=discord.ButtonStyle.success,emoji="😁")

    async def button_callback(self,button,interaction):
        await button.response.send_message('you click in smile button')


@client.tree.command(name='emoji_button',guild=guild_id)

async def start_buttons(interactions:discord.Interaction):

    await interactions.response.send_message(view=view())

client.run('MTQxNjY1MDE3MjY2MTc2NDEwOA.G20Xuh.LhXqMFG5pGKGfSQ2LyfmYBwPH25EFtieJunbf0')