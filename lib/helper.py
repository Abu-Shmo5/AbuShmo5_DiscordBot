import os
import json
import discord

class Helper():
    def is_guild(guild: discord.Guild | int | None) -> bool:
        return guild is not None
    
    def load_config():
        if not os.path.isfile("config.json"):
            with open("config.json", "w") as file:
                file.write("{}")
        with open("config.json", "r") as file:
            return json.loads("".join(file.readlines()))
        
    def save_config(config):
        with open("config.json", "w") as file:
            file.write(json.dumps(config))