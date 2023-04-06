import openai

with open ("keys.txt") as f:
	# coverting our text file to list of linew
	lines = f.read().split ('\n')
	#open ai api key
	openai.api_key = lines[0]
	# discord token
	DISCORD_TOKEN = LINES[1]
	# CLOSE THE FILE
	
f.close()
elif client.user.mentioned_in(message):
response = openai.Image.create(
	prompt="sunny day on a new york city beacha , vitage vibes, colors",
	n+1,
	size ="1024x1024"
)
image_url = response['data'][0]['url']
print (image_url)
#await message.channel.send(image_url)

#client.run(DISCORD_TOKENS)