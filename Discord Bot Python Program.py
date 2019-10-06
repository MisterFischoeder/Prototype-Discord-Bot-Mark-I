import discord
# importing commands functionality
from discord.ext import commands

# made it possible for you to either mention the bot or use the prefix ! for commands
client = commands.Bot(commands.when_mentioned_or('!'))

# minor spelling edit for "client"
@client.event
async def on_ready():
	print("The bot is ready!")
	await client.change_prescence(game=discord.Game(name="Making a bot"))
	
# here's a very simple example of a command, which you can use by saying !ping on discord
@client.command()
async def ping(ctx):
	await ctx.send('Pong!')

# minor newline edit after @client.event
@client.event
async def on_message(message):
	#changed the check to ignore all bots
	if message.author.bot:
		return
	if message.content == "Hello":
		await client.send_message(message.channel, "World")
		
client.run(TOKEN)
