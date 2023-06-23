import discord
import random

async def rand_num(message, channel):
    if '?' in message or '.' in message or '!' in message:
        message= message[:-1]
    range = message.split('between')[1].split('and')
    first = int(range[0])
    second = int(range[1])
    random_number = random.randint(first, second)
    await channel.send(random_number)

async def assign_pronouns(message, author, channel):
    if '.' in message or '!' in message:
        message = message[:-1]
    pronouns = message.split('are')[1].strip()
    role = discord.utils.get(channel.guild.roles, name=pronouns)
    if role is None:
        await channel.guild.create_role(name=pronouns)
        role = discord.utils.get(channel.guild.roles, name=pronouns)
    await author.add_roles(role)
    await channel.send(f'Your role has been set to the pronouns: {pronouns}!')