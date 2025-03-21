import discord
import os
from dotenv import load_dotenv

class discordClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        if type(message.channel) == discord.DMChannel:
            print(f"id: {message.channel.id}\nFrom: {message.author} in DMs\nContent: {message.content}")
        elif type(message.channel) == discord.TextChannel:
            if message.channel.category:
                fromPath = f"{message.guild}.{message.channel.category}.{message.channel}"
            else:
                fromPath = f"{message.guild}.{message.channel}"
            print(f"id: {message.channel.id}\nFrom: {message.author} in {fromPath}\nContent: {message.content}")

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        print(payload.emoji.name)
        print(payload.member.name)

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        print(payload.emoji.name)
        print(payload.member.name)


if __name__ == "__main__":
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True

    client = discordClient(intents=intents)
    client.run(BOT_TOKEN)