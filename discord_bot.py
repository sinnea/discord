import os
import discord
from discord.ext import tasks
from dotenv import load_dotenv

class QuoteBot(discord.Client):
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')
        for server in self.guilds:
            with open("other_channels.txt", 'a') as f:
                f.write("\nServer: "+server.name+"\n")
                for channel in server.channels:
                    f.write("  \nChannel:"+channel.name+ "\n")
                    if isinstance(channel, discord.TextChannel):
                        async for message in channel.history():
                            f.write(f'    {message.author} in #{message.channel}: {message.content}\n')

        await self.close()


load_dotenv()
TOKEN = "GTc5AjQ3OTUxOTQzMTGwNjg2.G82mZ3.2OnCyYA5Vw97v-0WSlRoWICt_g2WwRBMyi4hdU"

client = QuoteBot()
client.run(TOKEN)
