import os
import discord
from dotenv import load_dotenv
from lib.helper import Helper

# TODO: Print Time with every message/command
# TODO: Slash For AutoComplete

class discordClient(discord.Client):
    command_prefix = "$"

    async def on_ready(self):
        # for member in self.get_all_members():
            # print(member, member.guild, member.mutual_guilds, member.guild_permissions.administrator)
        Helper.print(f'Logged on as {self.user}!')

    async def on_resume(self):
        # TODO: Print Time
        print("Resumed")

    async def on_disconnect(self):
        # TODO: Print Time
        print("Disconnected")

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
                message_splits = message.content.split(" ")
                message_splits_len = len(message_splits)
                if message_splits[0] == f"{self.command_prefix}help":
                    await message.channel.send(f"# Help\n{self.command_prefix}help to show commands \n{self.command_prefix}set-role to set messages role\n{self.command_prefix}set-welcome <channel> | Set Welcome Channel")
                elif message_splits[0] == f"{self.command_prefix}set-role":
                    if not message.author.guild_permissions.administrator:
                        await message.channel.send(f"{message.author.mention} does not have permission")
                        return
                    await message.channel.send(f"Hello {message.author}")
                    print(message.author.roles)
                    print("Such Roles")
                elif message_splits[0] == f"{self.command_prefix}set-welcome":
                    if not message.author.guild_permissions.administrator:
                        await message.channel.send(f"{message.author.mention} does not have permission")
                        return
                    print(message_splits[1])
                else:
                    print("Read")

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

if __name__ == "__main__":
    config = Helper.load_config()
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    intents.presences = True
    client = discordClient(intents=intents)
    client.run(BOT_TOKEN)