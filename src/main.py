import discord
import random
import dotenv
import os
import gpt
import dalle
from PIL import Image

import bot

# On mets les autorisations nécessaires
intents = discord.Intents().all()
intents.messages = True
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


CPATR = bot.Bot(command_prefix="!", description="discord's bot", intents=intents)









CPATR.run(os.getenv("TOKEN"))
