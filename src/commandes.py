import discord
from discord.ext import commands


class Commandes(commands.Bot):

     def __init__(self, bot):
         super().__init__(command_prefix="!", intents=bot.intents)
         self._bot_commands  = bot
         self._liste_commandes = [hello]
         self._liste_commandes_str = [str(el) for el in self._liste_commandes]

     async def exe_commandes(self, ligne, channel):
         liste_ligne = ligne.split()
         i = self._liste_commandes_str.index(liste_ligne[0][1:])
         await self._liste_commandes[i](channel, liste_ligne[1:])


playlist = []

@commands.command()
async def hello(channel, reste_ligne):
    await channel.send('Hello !')

@commands.command()
async def join(channel, reste_ligne):
    if str(channel.type) != "voice":
        await channel.send('Cette commande ne fonctionne que dans les salons vocaux !')
    try:
        await channel.connect()
    except discord.errors.ClientException:
        await channel.send('Je suis déjà dans ce salon vocal')

@commands.command()
async def leave(channel, reste_ligne):
    playlist = []
    await channel.disconnect()


@commands.command()
async def start(channel, reste_ligne):
    player = await discord.FFmpegOpusAudio.from_probe(playlist[0])
    channel.voice_client.play(player)
    del playlist[0]


@commands.command()
async def add(channel, reste_ligne):
    print(reste_ligne)
    for musique in reste_ligne:
        playlist.append(musique)
    print(playlist)


#vc.play(discord.FFmpegPCMAudio("Local Music file URL"))
