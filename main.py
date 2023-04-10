import discord
import random
import dotenv
import os
import gpt

# On mets les autorisations nécessaires
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


# On charge les vriables d'environnements du fichier de config 'config'
dotenv.load_dotenv(dotenv_path="./config")

bot_ident = os.getenv("BOT_IDENT")
id_general_channel = int(os.getenv("GENERAL_CHANNEL"))
gpt_channel = int(os.getenv("BOT_GPT_CHANNEL"))
openai_key = os.getenv("OPENAI_API_KEY")

chat_GPT = gpt.GPT(openai_key)
print(chat_GPT.reponse_a_question("Salut, ça va ?"))





@client.event
async def on_member_join(member):
	"""  Affiche un message de bienvenue """
	arrival_channel = client.get_channel(id_general_channel)
	await arrival_channel.send(content=f"Bienvenue sur mon serveur !\nEnfin le serveur de Milou Killer\nVeuillez accueillir <@{member.id}> !!")

@client.event
async def on_member_remove(member):
	""" Affiche un doux message d'au revoir """
	depart_channel = client.get_channel(id_general_channel)
	await depart_channel.send(content=f"Heureusement que {member.name} est parti, c'était vraiment un con")


@client.event
async def on_connect():
	print("Bot connecté !")


@client.event
async def on_message(message):
	# On evite que le bot ne se reponde a lui même
	if str(message.author) != bot_ident:

		channel = message.channel

		if "quoi" in message.content.lowwer():
			await channel.send("quoicoubeuh")

		if random.randint(1, 100) == 42:
			await channel.send('Mangez tous vos morts', delete_after=3)

		if "PING" == message.content.upper():
			await channel.send('Pong')
		elif "PONG" == message.content.upper():
			await channel.send('Ping')

		elif channel.id == gpt_channel:
			print("Question à Chat GPT")
			reponse = chat_GPT.reponse_a_question(message.content)
			await channel.send(reponse)





client.run(os.getenv("TOKEN"))
