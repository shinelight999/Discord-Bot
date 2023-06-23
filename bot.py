import os

import discord
import random
import traceback

from dotenv import load_dotenv
from functions import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if client.user.id != message.author.id:
        if client.user.mentioned_in(message):
            if 'quack' in message.content.lower():
                await message.channel.send('Quack!')
            elif 'hey' in message.content.lower():
                try:
                    await message.channel.send('Hey ' + f"<@{message.author.id}>" + '! What\'s up?')
                except Exception as e:
                    traceback.print_exception(e)
                    await message.channel.send('Hey! What\'s up?')
            elif 'commands' in message.content.lower():
                await message.channel.send('Here are my commands: ' + '\n' + '1. Hey' + '\n' + '2. Quack' + '\n' + '3. Commands' + '\n' + 
                                           '4. Random Number' + '\n' + '5. Random User' + '\n' + '6. Pronouns')
            elif 'random number' in message.content.lower():
                try:
                    await rand_num(message.content.lower(), message.channel)
                except Exception as e:
                    traceback.print_exception(e)
                    await message.channel.send("When asking for a random number please use the format: 'random number between x and y'")
            elif 'random user' in message.content.lower():
                random_user = random.choice(message.guild.members)
                await message.channel.send('The random user is: ' + random_user.mention)
            elif 'pronouns' in message.content.lower():
                try:
                    await assign_pronouns(message.content.lower(), message.author, message.channel)
                except Exception as e:
                    traceback.print_exception(e)
                    await message.channel.send('Please use the format: \'pronouns are x\'')
            else:
                await message.channel.send('I am sorry. I do not understand that command.')
client.run(TOKEN)