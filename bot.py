import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('Hello, I am a bot')

client.run('ODcxMjIwNTQ4MjEzMDIyNzMy.YQYJXQ.sQL-9VW29qusVMpK0Sr1BZC1Wp8')