import os
import discord
import discord.ext
import discord.ext.commands
from lib.helper import Helper
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

# TODO: Print Time with every message/command
# TODO: For Quran & Welcome
# https://github.com/xixi52/discord-canvas (https://support.glitch.com/t/custom-fonts-in-discord-bot/4840) 
# https://www.geeksforgeeks.org/adding-text-on-image-using-python-pil/
# https://stackoverflow.com/questions/65868573/how-to-send-custom-emojis-with-bot-discord-py-rewrite

class discordClient(commands.Bot):

    def __init__(self, command_prefix, *, help_command = ..., tree_cls = app_commands.CommandTree, description = None, allowed_contexts = ..., allowed_installs = ..., intents, **options):
        # super().__init__(command_prefix, help_command=help_command, tree_cls=tree_cls, description=description, allowed_contexts=allowed_contexts, allowed_installs=allowed_installs, intents=intents, **options)
        super().__init__(intents=intents, command_prefix=command_prefix)

    async def on_ready(self):
        Helper.print(f'Logged on as {self.user}!')
        await self.tree.sync()
        Helper.print("Tree sync done (On Ready)")

    async def on_resume(self):
        Helper.print("Resumed")

    async def on_disconnect(self):
        Helper.print("Disconnected")

    async def close(self):
        Helper.save_config(config)

    async def on_member_join(self, member: discord.Member):
        with open(f"./logs/users/profile_{member.id}.png", "wb") as f:
            f.write((await member.avatar.to_file()).fp.read())

        # TODO: Edit Image combined with profile
        # TODO: Send the Welcome Message

    async def on_raw_member_remove(self, payload):
        pass

    async def on_member_update(self, before, after):
        pass

    async def on_interaction(self, interaction: discord.Interaction):
        # print(interaction)
        pass

    async def on_message(self, message: discord.Message):
        if self.user == message.author:
            return # TODO: Might Need To be removed for loggin

        if type(message.channel) == discord.DMChannel:
            print(f"id: {message.channel.id}\nFrom: {message.author} in DMs\nContent: {message.content}")
        elif type(message.channel) == discord.TextChannel:
            if message.channel.category:
                fromPath = f"{message.guild}.{message.channel.category}.{message.channel}"
            else:
                fromPath = f"{message.guild}.{message.channel}"
            print(f"id: {message.channel.id}\nFrom: {message.author} in {fromPath}\nContent: {message.content}")

            if message.content[0:len(self.command_prefix)] == self.command_prefix:
                await client.process_commands(message)
                # message_splits = message.content.split(" ")
                # message_splits_len = len(message_splits)
                # if message_splits[0] == f"{self.command_prefix}help":
                #     await message.channel.send(f"# Help\n{self.command_prefix}help to show commands \n{self.command_prefix}set-role to set messages role\n{self.command_prefix}set-welcome <channel> | Set Welcome Channel")
                # elif message_splits[0] == f"{self.command_prefix}set-role":
                #     if not message.author.guild_permissions.administrator:
                #         await message.channel.send(f"{message.author.mention} does not have permission")
                #         return
                #     await message.channel.send(f"Hello {message.author}")
                #     print(message.author.roles)
                #     print("Such Roles")
                # elif message_splits[0] == f"{self.command_prefix}set-welcome":
                #     if not message.author.guild_permissions.administrator:
                #         await message.channel.send(f"{message.author.mention} does not have permission")
                #         return
                #     print(message_splits[1])
                # else:
                #     print("Read")

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if not Helper.is_guild(payload.guild_id):
            return # Roles Room is only in guilds
        
        print(f"Added {payload.emoji.name} By: {payload.user_id} - {payload.member}")
        # TODO:
        # Force Remove Reaction in case added to roles the can be togther Ex. Gender
        # self.get_channel(payload.channel_id).get_partial_message(payload.message_id).remove_reaction(emoji=payload.emoji, member=payload.member)
        # Send to member changing role failed
        # await message.author.send("Role Failed to be Added due to conflict")
        
        # roles = self.get_guild(payload.guild_id).roles
        # print(roles)
        # print(discord.utils.get(roles, name="t"))
        # payload.member.add_roles()

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if not Helper.is_guild(payload.guild_id):
            return # Roles Room is only in guilds
        
        print(f"Removed {payload.emoji.name} By: {payload.user_id} - {self.get_user(payload.user_id)}")
        # roles = self.get_guild(payload.guild_id).roles
        # print(roles)
        # print(discord.utils.get(roles, name="t"))
        # payload.member.remove_roles()

    async def quran(self):
        # embed = discord.Embed(title="Help", description=f"{self.command_prefix}help to show commands \n{self.command_prefix}set-role to set messages role")
        # embed.colour = discord.colour.Color.blue()
        # await message.channel.send(embed=embed)
        pass

intents = discord.Intents.all()
client = discordClient(intents=intents, command_prefix="/")

@client.tree.command(name="help", description="help the bot")
async def help(interaction: discord.Interaction):
    # print(interaction)
    commands = []
    for command in client.tree._get_all_commands():
        commands.append(f"{command.name}: {command.description}")
    await interaction.response.send_message("\n".join(commands))

@client.tree.command(name="ping", description="ping the bot")
async def ping(interaction: discord.Interaction):
    print(interaction)
    await interaction.response.send_message(f"Pong! Latency is {client.latency}")

@client.tree.command(name="quran", description="quran the bot")
async def quran(interaction: discord.Interaction):
    print(interaction)
    await interaction.response.send_message(f"Pong! Latency is {client.latency}")

@client.tree.command(name="athkar", description="athkar the bot")
async def athkar(interaction: discord.Interaction):
    print(interaction)
    await interaction.response.send_message(f"Pong! Latency is {client.latency}")

if __name__ == "__main__":
    config = Helper.load_config()
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    client.run(BOT_TOKEN)