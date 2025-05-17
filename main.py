# main.py
import discord
from discord.ext import commands
import hashlib

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hash(ctx, *, message: str):
    hashed = hashlib.sha256(message.encode()).hexdigest()
    await ctx.send(f"🔐 SHA-256: `{hashed}`")

# Thay YOUR_TOKEN_HERE bằng token thật của bot discord ở dưới nha
bot.run("YOUR_TOKEN_HERE")
