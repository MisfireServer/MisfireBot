import os
from typing import Union

import aiohttp
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()


client = commands.Bot(".")


@client.command()
async def move(
        ctx : commands.Context, 
        channel: Union[discord.TextChannel, int],
        message : int
    ):

    """
    Moves a message from one channel to another
    Supports cross server


    You must be in the same channel as the message when running the commands

    Usage:
        .move [message_id] [channel(if in server), channel_id(if from another server)]

    """

    
    # Check if the channel is discord.TextChannel or int
    if isinstance(channel, int):
        cha = await client.fetch_channel(channel)
    else:
        cha: discord.TextChannel = channel

    # Fetches the message
    msg: discord.Member = await ctx.channel.fetch_message(message)
    name = msg.author.name
    
    # checks for an avatar
    if msg.author.avatar is not None:
        avatar = msg.author.avatar.url

        # Get the avatar url
        async with aiohttp.ClientSession() as session:
            async with session.get(avatar) as resp:
                avatar_bytes = await resp.read()
        
        avatar_bytes = bytes(avatar_bytes)

    else:
        avatar_bytes = None

    webhook = await cha.create_webhook(name=name, avatar=avatar_bytes)

    # If the message is none then pass 
    if msg.content is None or msg.content == "":    
        pass
    else:
        await webhook.send(content=msg.content)

    # If the message has attachments then send those too
    if msg.attachments is not None:
        for i in msg.attachments:
            await webhook.send(i.url)

    # Delete the webhook since discord has a webhook limit
    await webhook.delete()


@client.event
async def on_ready():
    print("Bot is online")


client.run('ODk5NjY1MDc3OTQ5NTg3NDU2.YW2EZQ.ikmT-zKTZwxs9UNgNYGD9BGcJlA')