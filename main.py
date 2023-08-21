import discord
from discord.ext import commands
import yahoo_api

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Permission to Read/Send messages and embed links for excel sheets or graphs. Integer = 19456
permissions = discord.Permissions(permissions=19456)

@bot.event
async def on_ready():
    print(f"Bot connected to Discord as {bot.user.name}")

# Name of command is func name
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def update(ctx, *, message=yahoo_api.aapl):
    if len(message) <= 1800:
        # Send the message as a single message if it is within the limit
        await ctx.send(f"```{chunk}```")
    else:
        # Split the message into chunks of 2000 characters or less and send each chunk as a separate message
        chunks = [message[i:i+1800] for i in range(0, len(message), 1800)]
        for chunk in chunks:
            await ctx.send(f"```{chunk}```")

bot.run('PRIVATE_DISCORD_BOT_KEY')
