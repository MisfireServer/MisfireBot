from ast import alias
import discord
import random
from discord.ext import commands
import qrcode
import numexpr as ne
import numpy
import aiohttp
import asyncio
import datetime
from random import randrange
import requests
from pyfiglet import figlet_format, FontError, FontNotFound

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["flip", "coin"])
    async def coinflip(self, ctx):
        """ Coinflip! """
        coinsides = ["Heads", "Tails"]
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

    @commands.command()
    async def reverse(self, ctx, *, text: str):
        """ !poow ,ffuts esreveR
        Everything you type after reverse will of course, be reversed
        """
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await ctx.send(f"🔁 {t_rev}")

    @commands.command(aliases=['qr'])
    async def qrcode(self, ctx, *, url):
        await ctx.message.delete()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(str(url))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black",
                            back_color="white").convert('RGB')
        img.save('qrcode.png')
        await ctx.send(file=discord.File('qrcode.png'))


    @commands.command(aliases=["calculator"])
    async def calc(self, ctx, *, text: str):
        calc = ne.evaluate(text)
        msg = int(calc)
        await ctx.send(msg)

    @commands.command(Hidden=True)
    @commands.has_guild_permissions(administrator=True)
    async def say(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text)



    @commands.command(aliases=['rockpaperscissors'], help="Play Rock Paper Scissors")
    async def rps(self, ctx, rps: str):
        choices = ["rock", "paper", "scissors"]
        cpu_choice = random.choice(choices)
        em = discord.Embed(title="Rock Paper Scissors")
        rps = rps.lower()
        if rps == 'rock':
            if cpu_choice == 'rock':
                em.description = "It's a tie!"
            elif cpu_choice == 'scissors':
                em.description = "You win!"
            elif cpu_choice == 'paper':
                em.description = "You lose!"

        elif rps == 'paper':
            if cpu_choice == 'paper':
                em.description = "It's a tie!"
            elif cpu_choice == 'rock':
                em.description = "You win!"
            elif cpu_choice == 'scissors':
                em.description = "You lose!"

        elif rps == 'scissors':
            if cpu_choice == 'scissors':
                em.description = "It's a tie!"
            elif cpu_choice == 'paper':
                em.description = "You win!"
            elif cpu_choice == 'rock':
                em.description = "You lose!"

        else:
            em.description = "Invalid Input"

        em.add_field(name="Your Choice", value=rps)
        em.add_field(name="Bot Choice", value=cpu_choice)
        await ctx.send(embed=em)



    @commands.command(aliases=['yahornah', 'yn'], extras={"category":"Fun"}, usage="yesorno [question]", help="This command makes a small poll which users can vote either yes, or no", description="Makes a Yah or Nah poll")
    async def yesorno(self, ctx, *, message):
        msg = await ctx.send(embed=discord.Embed(title="Yah or Nah?", description=message))
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

    @commands.command(aliases=["doggo"], help = "It shows you a Dog photo as well as a fact") #shows a dog photo and a fact
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()
            # This time we'll get the fact request as well!
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()

        embed = discord.Embed(title="Doggo!", color=discord.Color.purple())
        embed.set_image(url=dogjson['link'])
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed)

    @commands.command(help = "It shows you a cat photo as well as a fact") #shows cat photo and fact
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            catjson = await request.json()
        # This time we'll get the fact request as well!
            request2 = await session.get('https://some-random-api.ml/facts/cat')
            factjson = await request2.json()

        embed = discord.Embed(title="Cat!", color=discord.Color.purple())
        embed.set_image(url=catjson['link'])
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed)


    @commands.command(help = "It shows you a panda photo as well as a fact") #shows cat photo and fact
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/panda')
            Pandajson = await request.json()
        # This time we'll get the fact request as well!
            request2 = await session.get('https://some-random-api.ml/facts/panda')
            factjson = await request2.json()

        embed = discord.Embed(title="Panda!", color=discord.Color.purple())
        embed.set_image(url=Pandajson['link'])
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed)


    @commands.command(help = "It shows you a koala photo as well as a fact") #shows cat photo and fact
    async def koala(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/koala')
            koalajson = await request.json()
        # This time we'll get the fact request as well!
            request2 = await session.get('https://some-random-api.ml/facts/koala')
            factjson = await request2.json()

        embed = discord.Embed(title="koala!", color=discord.Color.purple())
        embed.set_image(url=koalajson['link'])
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed)


    @commands.command(help = "It shows you a fox photo as well as a fact") #shows cat photo and fact
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/fox')
            foxjson = await request.json()
        # This time we'll get the fact request as well!
            request2 = await session.get('https://some-random-api.ml/facts/fox')
            factjson = await request2.json()

        embed = discord.Embed(title="fox!", color=discord.Color.purple())
        embed.set_image(url=foxjson['link'])
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed)

    @commands.command(help = "It shows you a bird photo as well as a fact") #shows cat photo and fact
    async def bird(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/birb')
            birdjson = await request.json()
        # This time we'll get the fact request as well!
            request2 = await session.get('https://some-random-api.ml/facts/bird')
            factjson = await request2.json()

        embed = discord.Embed(title="bird!", color=discord.Color.purple())
        embed.set_image(url=birdjson['link'])
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed)



    
    @commands.command(aliases=['pie'])
    async def catch(self,ctx):
        """Catch the pie, by reacting. Dont't drop it!"""
        em = discord.Embed(color=discord.Color.orange())
        em.add_field(name='🥧  __Catch The Pie Game__  🥧', value='To catch the pie you must simply react with the emoji, when it appears. Click as fast as you can and see how fast you caught it... \n**Good Luck!** \n\nHere we go in ?time...', inline=False)
        pie1 = await ctx.send(embed=em)


        await asyncio.sleep(randrange(5))
        await pie1.add_reaction('🥧')

        def check(reaction, user):
            self.reacted = reaction.emoji
            return user == ctx.author and str(reaction.emoji)

        before_wait = datetime.datetime.now()
        reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
        after_wait = datetime.datetime.now()
        time_delta = after_wait - before_wait
        time_taken = time_delta.total_seconds()

        em = discord.Embed(color=discord.Color.orange())
        em.add_field(name='🥧  __Catch The Pie Game__  🥧', value=f'To catch the pie you must simply react with the emoji, when it appears. Click as fast as you can and see how fast you caught it... \n**Good Luck!** \n\nYou caught it in **{round(time_taken, 5)} seconds**', inline=False)
        await pie1.edit(embed=em)


    
    @commands.command(aliases=['hack'])
    async def hecker(self, ctx, member: discord.Member):
        """Hack someone and get their details."""
        used_words = ['Nerd','Sucker','Noob','Sup','Yo','Wassup','Nab','Nub','fool','stupid','b1tch','fvck','idiot']
        mails = ['@gmail.com','@hotmail.com','@yahoo.com']

        hacking = await ctx.send(f"Hacking {member.name}....")
        await asyncio.sleep(1.55)
        await hacking.edit(content='Finding info....')
        await asyncio.sleep(1.55)
        await hacking.edit(content=f"Discord email address: {member.name}{random.choice(mails)}")
        await asyncio.sleep(2)
        await hacking.edit(content=f"Password: x2yz{member.name}xxy65")
        await asyncio.sleep(2)
        await hacking.edit(content=f'Most used words: {random.choice(used_words)}')
        await asyncio.sleep(1.55)
        await hacking.edit(content='IP address: 127.0.0.1:50')
        await asyncio.sleep(1.55)
        await hacking.edit(content='Selling information to the government....')
        await asyncio.sleep(2)
        await hacking.edit(content=f'Reporting {member.name} to Discord for violating ToS')
        await asyncio.sleep(2)
        await hacking.edit(content='Hacking medical records.....')
        await asyncio.sleep(1.55)
        await hacking.edit(content=f"{ctx.author.mention} successfully hacked {member.mention}")
        await ctx.send("The ultimate, totally real hacking has been completed!")

    @commands.command(aliases=["ss"])
    async def screenshot(self, ctx, *, url):
        """Takes a screenshot from a given URL."""
        await ctx.send(f"https://image.thum.io/get/https://{url}")


    @commands.command(aliases=["boredom"])
    async def bored(self,ctx):
        BASE_URL = "https://www.boredapi.com/api/activity?"
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            data = response.json()
            activity = data['activity']
            accessibility = data['accessibility']
            type = data['type']
            participants = data['participants']
            price = data['price']
        

            e = discord.Embed(
                title=f"If your bored, you should try {activity}",
                color=discord.Colour.blue() )
            e.add_field(name="Accessibility", value=accessibility)
            e.add_field(name="Type", value=type)
            e.add_field(name="Participants", value=participants)
            e.add_field(name="Price", value=price)
            await ctx.send(embed=e)
        
        else:
            # showing the error message
            await ctx.send("I've had a connection issue Sir.")

    @commands.group(pass_context=True, invoke_without_command=True)
    async def ascii(self, ctx, *, msg):
        """Convert text to ascii art."""
        if ctx.invoked_subcommand is None:
            if msg:
                font = "big"
                msg = str(figlet_format(msg.strip(), font=font))
                if len(msg) > 2000:
                    await ctx.send('Message too long, RIP.')
                else:
                    await ctx.message.delete()
                    await ctx.send('```\n{}\n```'.format(msg))
            else:
                await ctx.send(
                               'Please input text to convert to ascii art. Ex: ``>ascii stuff``')

    @commands.group(pass_context=True, invoke_without_command=True)
    async def slantascii(self, ctx, *, msg):
        """Convert text to ascii art."""
        if ctx.invoked_subcommand is None:
            if msg:
                font = "slant"
                msg = str(figlet_format(msg.strip(), font=font))
                if len(msg) > 2000:
                    await ctx.send('Message too long, RIP.')
                else:
                    await ctx.message.delete()
                    await ctx.send('```\n{}\n```'.format(msg))
            else:
                await ctx.send(
                               'Please input text to convert to ascii art. Ex: ``>ascii stuff``')


def setup(bot):
    bot.add_cog(Fun(bot))