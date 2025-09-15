import discord 

class client(discord.Client):

    async def on_ready(self):

        print(f'congrat a {self.user} bot runs in your server')

    

    async def on_message(self,message): #when member send message

        print(f'Message from {message.author} : {message.content}')

        if message.author==self.user:
            return     #if bot who send message don't reblay
        
        if message.content.startswith('hellow'):
            await message.channel.send(f'Hi there {message.author}')






intens=discord.Intents.default()
intens.message_content=True

my_client=client(intents=intens)
my_client.run('MTQxNjY1MDE3MjY2MTc2NDEwOA.G20Xuh.LhXqMFG5pGKGfSQ2LyfmYBwPH25EFtieJunbf0')