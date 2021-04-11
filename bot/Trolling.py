import os

import discord
from discord.ext import commands
from discord.ext import tasks
import string
import random



intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('bot ready')


@client.event
async def on_message(msg):
    if(msg.content=='!troll' and False):
        channels = msg.guild.channels
        users = msg.guild.members
        namesList=[]
        for name in users:
            namesList.append(name.name)
        
        iterator = 0
        
        for channel in channels:
            print(channel.name)
            iterator+=1
            chnlname=''.join(random.choice(string.ascii_lowercase) for i in range(10))
            await channel.edit(name=chnlname)
            print('running change')
        iterator2=0
        for user in users:
            iterator2+=1
            try:
                await user.edit(nick=random.choice(namesList))
            except:
                print('failed ot set tag for a user:{0}'.format(user.name))
    if(msg.content=='distribute' and False):
        for role in msg.guild.roles:
            if(role.name=='Gamer'):
                for member in msg.guild.members:
                    await member.add_roles(role)

    if(msg.content=='!kick bot'):
        for member in msg.guild.members:
            print(member.nick)
            if(not member.nick == None):
                if('bot' in member.nick[0:3].lower()):
                    print(member.name,member.nick)
                    await member.kick(reason = "inactivity")
TOKEN = os.getenv('DISCORD_TOKEN')
client.run(TOKEN,bot=False)
