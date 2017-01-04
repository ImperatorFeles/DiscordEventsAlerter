import discord
import asyncio

client = discord.Client()

@client.event
@asyncio.coroutine 
def on_ready():
	print("Logged in as")
	print(client.user.name)
	print(client.user.id)
	print("-------")

@client.event
@asyncio.coroutine 
def on_message(message):
	if message.content.startswith("!test"):

		if message.server is None:
			yield from client.send_message(message.channel, "Hello, recruit.")
		else:
			yield from client.send_message(message.channel, "Hello, recruits. Currently I am not assisting this guild with anything, but I should be able to soon.")

client.run("MjY2MzIxOTI2ODMyNTIxMjE2.C08AeQ.ySY3Yhh9Cr9oKULGsTqw4uDTZkg")