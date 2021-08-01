import discord
import requests
import json

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

client.run('ODcxMjIwNTQ4MjEzMDIyNzMy.YQYJXQ.Vs7-DxZxEXfYG-UXg9NnkOsy3a0')