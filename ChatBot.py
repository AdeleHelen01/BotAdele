import openai
import discord

openai.api_type ="azure"
openiai.api_version = "2023-03-15-preview"

with open("keys.txt") as f:
	# converting oue text file to a list of lines
	lines = f.read(). split('\n')
	#openai api key
	openai.api