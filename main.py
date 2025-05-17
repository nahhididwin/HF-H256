import discord
from discord import app_commands
import hashlib
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")


class MyClient(discord.Client):

    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        synced = await self.tree.sync()
        print(f"Đã sync {len(synced)} lệnh slash")


client = MyClient()


@client.tree.command(name="hash", description="Mã hóa SHA-256 chuỗi văn bản")
@app_commands.describe(text="Chuỗi cần mã hóa")
async def hash_sha256(interaction: discord.Interaction, text: str):
    hashed = hashlib.sha256(text.encode()).hexdigest()
    await interaction.response.send_message(f"SHA-256: `{hashed}`")


client.run(TOKEN)
