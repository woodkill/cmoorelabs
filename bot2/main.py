import discord
import requests
import asyncio

class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__()