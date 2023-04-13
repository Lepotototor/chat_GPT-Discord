import discord
from discord.ext import commands
import random
import dotenv
import os
import gpt
import dalle
from PIL import Image


intents = discord.Intents().all()
intents.members = True
intents.messages = True
intents.message_content = True

CPATR = commands.Bot(command_prefix="!", description="test", intents=intents)




# On charge les vriables d'environnements du fichier de config 'config'
dotenv.load_dotenv(dotenv_path="../config")

bot_ident = os.getenv("BOT_IDENT")
id_general_channel = int(os.getenv("GENERAL_CHANNEL"))
gpt_channel = int(os.getenv("BOT_GPT_CHANNEL"))
dalle_channel = int(os.getenv("BOT_DALLE_CHANNEL"))
openai_key = os.getenv("OPENAI_API_KEY")

chat_GPT = gpt.GPT(openai_key)
dall_e = dalle.DALLE(openai_key)





@CPATR.event
async def on_ready():
	print("Bot connecté !")
	general_channel = CPATR.get_channel(id_general_channel)
	print(general_channel)
	await general_channel.send("Coucou je suis de retour !")

@CPATR.event
async def on_disconnect():
	print("Bot déconnecté !")
	general_channel = CPATR.get_channel(id_general_channel)
	await general_channel.send("Je vais faire une petite sieste...")


@CPATR.event
async def on_member_join(member):
	"""  Affiche un message de bienvenue """
	arrival_channel = CPATR.get_channel(id_general_channel)
	await arrival_channel.send(content=f"Bienvenue sur mon serveur !\nEnfin le serveur de Milou Killer\nVeuillez accueillir <@{member.id}> !!")

@CPATR.event
async def on_member_remove(member):
	""" Affiche un doux message d'au revoir """
	depart_channel = CPATR.get_channel(id_general_channel)
	await depart_channel.send(content=f"Heureusement que {member.name} est parti, c'était vraiment un con")


@CPATR.command()
async def hello(ctx):
    print("dans la fonction")
    await ctx.send('Hello!')

@CPATR.command()
async def join(ctx):
    #if ctx.type != "voice":
        #await ctx.send('Cette commande ne fonctionne que dans les salons vocaux !')

    voice_channel = ctx.author.voice.channel
    print(voice_channel)
    if bot.voice is None:
        bot.voice = await voice_channel.connect()
    else:
        await bot.voice.move_to(voice_channel)







CPATR.run(os.getenv("TOKEN"))
