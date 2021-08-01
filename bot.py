import discord
import requests
import json
import asyncio

client = discord.Client()


def get_question():
    qs = ''
    id = 1
    answer = 0
    response = requests.get("http://127.0.0.1:8000/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + '\n'

    for item in json_data[0]['answer']:
        qs += str(id) + ". " + item['answer'] + "\n"
        if item['is_correct']:
            answer = id
        id += 1
    return(qs, answer)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$question'):
        question, answer = get_question()
        await message.channel.send(question)

        def check(m):
            return m.author == message.author and m.content.isdigit()
        
        try:
            guess = await client.wait_for('message', check=check, timeout=2.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry, you took too long')

        if int(guess.content) == answer:
            await message.channel.send('You are correct!')
        else:
            await message.channel.send('Oops. That is not right.')

client.run('ODcxMjIwNTQ4MjEzMDIyNzMy.YQYJXQ.Dzru7p5n6Xqq1E-cqnNDvRncaN4')