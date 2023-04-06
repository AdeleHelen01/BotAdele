import requests
import time
import os
#from PIL import Image
import discord

# create an object that will control our discord bot
client = discord.Client(intents=discord.Intents.default())

with open("keys.txt") as f:
    # converting our text file to a list of lines
    lines = f.read().split('\n')
    # openai api key
    api_key = lines[0]
    # discord token
    DISCORD_TOKEN = lines[1]
    api_base = lines[2]
# close the file
f.close()


api_version = '2022-08-03-preview'

@client.event
async def on_ready():
    # print out nice statment saying our bot is online (only in command prompt)
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # this prevents inifinte loops of bot talking to bot
    # if author of the message is the bot, don't do anything
    if message.author == client.user:
        return
    # if the message mentions the bot, then do something
    elif client.user.mentioned_in(message): 
        url = "{}dalle/text-to-image?api-version={}".format(api_base, api_version)
        headers= { "api-key": api_key, "Content-Type": "application/json" }
        body = {
            "caption": message.content,
            "resolution": "1024x1024"
        }
        submission = requests.post(url, headers=headers, json=body)
        operation_location = submission.headers['Operation-Location']
        retry_after = submission.headers['Retry-after']
        status = ""
        while (status != "Succeeded"):
            time.sleep(int(retry_after))
            response = requests.get(operation_location, headers=headers)
            status = response.json()['status']
        image_url = response.json()['result']['contentUrl']
        print(image_url)
        # data = requests.get(image_url).content
# 
        # f = open('img01.jpg', 'wb')
        # f.write(data)
        # f.close()
        await message.channel.send("Elvis in a car driving on a sumny day!", file=discord.File('img01.jpg'))

client.run(DISCORD_TOKEN)