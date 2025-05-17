import discord
import hashlib

# Thay bằng token bot của bạn nha:D
TOKEN = "YOUR_BOT_TOKEN"

intents = discord.Intents.default()
intents.message_content = True  

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot đã đăng nhập dưới tên: {client.user}")

@client.event
async def on_message(message):
    # skip tin nhắn của chính bot
    if message.author == client.user:
        return

    # if bắt đầu bằng "/hash:"
    if message.content.startswith("/hash:"):
        raw_text = message.content[len("/hash:"):].strip()
        if raw_text == "":
            await message.reply("⚠️ Bạn chưa nhập nội dung để hash!")
            return
        
        # Hash bằng SHA-256
        hash_object = hashlib.sha256(raw_text.encode())
        hash_hex = hash_object.hexdigest()
        
        await message.reply(f"🔒 SHA-256:\n```{hash_hex}```")

client.run(TOKEN)
