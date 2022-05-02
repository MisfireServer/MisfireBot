import discord
from discord.ext import commands
import json
import random
import os


client = commands

class Misfire(commands.Cog):
    def __init__(self, client): 
        self.client = client 
    

@client.command(help = "All the info of Artica")
async def Arctica(ctx):
    await ctx.send("Here is us on the map")
    await ctx.send(file=discord.File('Map/Arctica.PNG'))
    await ctx.send("welcome to the artica \n no weponds are allowed to be inyour hand  4dia fine \n no going to privet areas 4dia + fine \n you leave when told \n if you are here you agree to all this as well as we can kill you at anytime with out warning \n no pets allowed \n no fire allowed")
    await ctx.send("National beverage: Vodka")

@client.command(help = "All the info of Mittelreich")
async def Mittelreich(ctx):
    await ctx.send("━━━━━━━━━━━☆☆━━━━━━━━━━━")
    await ctx.send(" Kingdom of Mittelreich")
    await ctx.send(file=discord.File('Map/mittelreich.png'))
    await ctx.send("╭────── ✠ ────── \nKingdom of Mittelreich\nSole current Mediterranean power\nUndergoing revival\nNew members welcome\nMultiple under-construction cities\nEnglish & German chats\n╰────── ✠ ──────")
    
    
@client.command(help = "All the info of Melisima")
async def Melisima(ctx):
    await ctx.send("Here is us on the map")
    await ctx.send(file=discord.File('Map/Melisima.png'))
    await ctx.send(file=discord.File('Map/Melisima1.png'))
    await ctx.send("No entering (unless permission or in alliance/empire) \n No mining in country \n No using farms (unless in alliance/empire) \n No opening chests \nNo going in buildings like castles or houses (unless in alliance/empire) \n No fire \n No placing blocks (unless permission) \n No bows or crossbows \n No killing raiders or creepers (unless in alliance/empire) \n No using villagers (unless permission) \n No killing players \n If we catch anyone breaking the rules we will fine you 1-5 netherite (depends on how severe it was)")

@client.command(help = "A map of the world",aliases=["Full_Map", "fullmap"])
async def full_map(ctx):
    await ctx.send("Here is the map")
    await ctx.send(file=discord.
    File('Map/map.jpg'))
  

#Report Bug

@client.command(help = "Report a bug on the server to staff.")
async def bug(ctx, *, content:str):
    channel = client.get_channel(899912659217035264)
    await channel.send(f"{content} **is a bug reported by {ctx.message.author}**")

@commands.has_role(900406761427705866) 
@client.command(help = "Declare War")
async def war(ctx, *, content:str):
    channel = client.get_channel(900040716342947870)
    await channel.send(f" <@&886218713458700298> **War Declared **{content} **War was declared by {ctx.message.author}**")

@commands.has_role(829075320870666300) 
@client.command(hidden=True)
async def announcements(ctx, *, content:str):
    channel = client.get_channel(829075330807234582)
    await channel.send({content})

@client.command() #mute
async def mute(member: discord.Member):
	await client.server_voice_state(member,mute=True)
	await client.say('{} has been muted.'.format(member.mention))

@client.command() #unmute
async def unmute(member: discord.Member):
	await client.server_voice_state(member,mute=False)
	await client.say('{} has been unmuted.'.format(member.mention))


@commands.has_permissions(kick_members=True) #kick whith permitions
@client.command()
async def warn(ctx, user: discord.User, *, message=None):
    message = message or "This Message is sent via DM"
    await discord.User.send(user, message + (f"** Warned by {ctx.message.author}**"))

@client.command(aliases=["Ip"])
async def ip(ctx):
    await ctx.send('157.90.4.54:25779') 

@client.command()
async def map(ctx):
    await ctx.send('MapMisfire.ddnsgeek.com')

@client.command(aliases=["8ball", "eightball", "eight_ball", "Eight_ball"]) #8ball games
async def _8ball(ctx, *, question):
    responses = ['magic eight ball maintains Signs point to yes.',
                 'magicball affirms My reply is no.',
                 'magic ball answers Signs point to yes.',
                 'magicball affirms Yes definitely.',
                 'magicball affirms Yes.',
                 '8 ball magic said Most likely.',
                 'magic ball answers Very doubtful.',
                 'magic 8 ball answers Without a doubt.',
                 'mystic eight ball said Most likely.',
                 "magic ball answers Don't count on it.",
                 'Magic ball says 100% No',
                 'Magic ball does not know have you tryed google?',
                 "Its not looking so good",
                 "Don't ask The_AI as he will not know"]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=["Fun_facts", 'fun facts','funfacts'],help = "It tells you misfire fun facts") #8ball games
async def fun_facts(ctx,):
    responses = ['TheAI was the first person other than azones to join the Misfire discord server',
                 'Miss Tiger getting muted first (on the server).',
                 "Azones and Miss Tiger once had a hour debate about taxes for misfire",
                 'G9. the boss going to start a world war o on the 6th of april 2022',
                 "The Misfire server started on a realm",
                 "There was a season before season one with azones Alki and another 2 freinds",
                 "I am the best bot on the server and have a great inventor",
                 "This bot originally was only online while mic was awake",
                 "G9. the boss was the first to start an anarchist country",
		         "SplashBrotherBE was the first winner of the halloween events",
                 "There are multiple easter egg commands with this bot",
                 "Did you know there was a case of greafing on this server but it took the staff less than half a day to work out who",
		         "SplashBrotherBE remains the one and only mayor of MisFire City. (season one)",
		         "Miss Tiger used to be best fasjion creator of MisFire City.(season one)",
                 "Ai is the maker of the misfire class datapack"]
    await ctx.send(f'Fact: {random.choice(responses)}')


#unban user 
@client.command(help = "Unbans a user from the server")
@commands.has_permissions(kick_members=True)
async def unban(ctx, user: discord.User, *, reason=None):
    await ctx.guild.unban(user, reason=reason)



@client.command(hidden = True)
async def bond(ctx):
    await ctx.send('Hello Mr.Bond I was not expecting you, currenty Misfire does not have a secret service. I hear Artica is lovely this time of year.')

@client.command(hidden = True)
async def mic(ctx):
    await ctx.send("Can't i hide anywhere around here, I need a vacation soon")

@client.command(hidden = True)
async def easter_egg(ctx):
    await ctx.send("Did you think i would just give you the easter eggs. have fun finding them and good luck.")


@client.command(hidden = True)
async def Ai(ctx):
    await ctx.send('"My favourite thing to say is hmmm" -Ai 2021')

@client.command(hidden = True)
async def tank(ctx):
    await ctx.send('TANK TANK TANK')


@client.command(hidden = True)
async def pog(ctx):
    await ctx.send('Pog Pog Pog')



    
def setup(client):
    client.add_cog(Misfire(client))
