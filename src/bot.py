import discord
from discord.ext import commands
import dotenv
import random
import os
import gpt
import dalle
from PIL import Image
import commandes


class Bot(commands.Bot):

    def __init__(self, command_prefix, description, intents):
        super().__init__(command_prefix=command_prefix, description=description, intents=intents)

        self._command_prefix = command_prefix

        # On charge les vriables d'environnements du fichier de config 'config'
        dotenv.load_dotenv(dotenv_path="../config")

        self._bot_ident = os.getenv("BOT_IDENT")
        self._id_general_channel = int(os.getenv("GENERAL_CHANNEL"))
        self._gpt_channel = int(os.getenv("BOT_GPT_CHANNEL"))
        self._dalle_channel = int(os.getenv("BOT_DALLE_CHANNEL"))
        self._openai_key = os.getenv("OPENAI_API_KEY")

        self._chat_GPT = gpt.GPT(self._openai_key)
        self._dall_e = dalle.DALLE(self._openai_key)

        self._exe_commandes = commandes.Commandes(self)



    @commands.command(name="join")
    async def join(self, ctx):
        print("kjoin")
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            return await ctx.send('You need to be in a voice channel to use this command!')

        voice_channel = ctx.author.voice.channel
        if self.voice is None:
            self.voice = await voice_channel.connect()
        else:
            await self.voice.move_to(voice_channel)

    @commands.command()
    async def leave(self, ctx):
        print("leave")
        await self.song_queue.put(None)
        await self.voice.disconnect()
        self.voice = None

    @commands.command()
    async def ping(self, ctx):
            await ctx.send('troubadour!')



    async def on_member_join(self, member):
    	"""  Affiche un message de bienvenue """
    	arrival_channel = self.get_channel(self._id_general_channel)
    	await arrival_channel.send(content=f"Bienvenue sur mon serveur !\nEnfin le serveur de Milou Killer\nVeuillez accueillir <@{member.id}> !!")

    async def on_member_remove(self, member):
    	""" Affiche un doux message d'au revoir """
    	depart_channel = self.get_channel(self._id_general_channel)
    	await depart_channel.send(content=f"Heureusement que {member.name} est parti, c'était vraiment un con")


    async def on_ready(self):
    	print("Bot connecté !")
    	general_channel = self.get_channel(self._id_general_channel)
    	print(general_channel)
    	await general_channel.send("Coucou je suis de retour !")

    async def on_disconnect(self):
    	print("Bot déconnecté !")
    	general_channel = self.get_channel(self._id_general_channel)
    	await general_channel.send("Je vais faire une petite sieste...")


    async def on_message(self, message):
    	# On evite que le bot ne se reponde a lui même
    	if str(message.author) != self._bot_ident:

            channel = message.channel

            if est_commande(message.content, self._command_prefix):
                await self._exe_commandes.exe_commandes(message.content, channel)
                #commande_bot(self, message.content, channel)

            elif "quoi" in message.content.lower():
                await channel.send("quoicoubeuh")

            if random.randint(1, 100) == 42:
                await channel.send('Mangez tous vos morts', delete_after=3)


            if "PING" == message.content.upper():
                await channel.send('Pong')
            elif "PONG" == message.content.upper():
                await channel.send('Ping')

            elif channel.id == self._gpt_channel:
                print("Question à Chat GPT")
                try:
                    reponse = await self._chat_GPT.reponse_a_question(message.content)
                    await channel.send(reponse)
                except:
                    await channel.send("Désolé je n'arrive pas à répondre à votre question")

            elif channel.id == self._dalle_channel:
                print("Générer image")
                try:
                    image = await self._dall_e.générerImage(message.content)
                    image.save("dalle.png")

                    await channel.send(file=discord.File("dalle.png"))
                except:
                    await channel.send("Génération de l'image impossible")




def est_commande(message, signe):
    if (len(message) == 1) and (message[0] != signe):
        return False
    elif message[0] == signe:
        print("commande détectée")
        return True
    return est_commande(message[1:], signe)




def commande_bot(bot, message, channel):
    self._exe_commandes(channel)
