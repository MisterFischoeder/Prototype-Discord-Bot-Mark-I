import discord
client = discord.Client()
@cliet.event
async def on_ready():
	print("The bot is ready!")
	await client.change_prescence(game=discord.Game(name="Making a bot"))
	
@client.eventasync def on_message(message):
	if message.author ==client.user:
		return
	if message.content == "Hello":
		await client.send_message(message.channel, "World")
		
client.run(TOKEN)
