import discord
from discord.ext import commands
import dotenv
import os
dotenv.load_dotenv(".env")

TOKEN=os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/67", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "chirlie" in message.content.lower() or "kirk" in message.content.lower():
        await message.channel.send("WE ARE CHIRLIE KIRK")
    
    if "67" in message.content:
        await message.channel.send("SIX SEVEN")
    
    if "hasina" in message.content.lower():
        await message.channel.send("Did you mean Sanigga?")
    
    if "brat" in message.content.lower():
        await message.channel.send("Brat aint Sigma")
        
    if "hasnat" in message.content.lower():
        await message.channel.send("Hasnat is the real Sigma")
    if "guzboi" in message.content.lower():
        await message.channel.send("Yousuf")

    
if TOKEN:
    bot.run(token=TOKEN)