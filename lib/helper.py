import os
import json
import time
import discord
from lib import cli_colouring

# TODO: Sqlite3 Commands

class Helper():
    def get_time() -> str:
        return time.strftime(f"[%Y-%m-%d %H:%M:%S]", time.localtime(time.time()))

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

    def print(content):
        print(f"{cli_colouring.EFFECTS.FOREGROUND_BRIGHT_BLACK.value}{Helper.get_time()}{cli_colouring.EFFECTS.CLEAR.value} {content}")