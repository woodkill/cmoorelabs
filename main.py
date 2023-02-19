import asyncio
import discord
import config
import os

from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print("Online.")


@bot.event
async def on_message(message: discord.Message):
    await bot.process_commands(message)
    if message[0] == ".":
        return
    if message.author == bot.user:
        return
    await message.channel.send("hello friend.")


async def load():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")


async def set_up():
    print("setting up...")


async def main():
    await load()
    await set_up()
    await bot.start(config.TOKEN)

asyncio.run(main())
