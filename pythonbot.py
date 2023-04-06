import openai
import discord

GUILD = '{AdeleCTA-server}'

client = discord.Client(intents = discord.Intents.default())

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif client.user.mentioned_in(message):
        # chat completions with chat-gpt
        # response = openai.ChatCompletion.create(
        #     model = 'gpt-3.5-turbo',
        #     messages=[
        #         {"role": "system", "content": "I am wonderful."},
        #         {"role": "user", "content": "Life is an Adventure"},
        #         {"role": "assistant", "content": "it is always sunny in London"},
        #         {"role": "user", "content": "What a wonderful life"}
        #     ]
        # )

        await message.channel.send('what is the time in New York City.')
        print(message.content)




with open('keys.txt') as f:
    # converting out text file to a list of lines
    lines = f.read().split('\n')
    # openai api key
    openai.api_key = lines[0]
    # discord token
    discord_token = lines[1]
#close the file
f.close()



client.run(discord_token)