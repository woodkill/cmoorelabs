import discord
import requests
import asyncio
import logging

import mytoken

logger = logging.getLogger('discord')
logging.basicConfig(level=logging.INFO)

class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        print('setup_hook')

    async def on_ready(self):
        print('MyClient online!')
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def my_background_task(self):
        await self.wait_until_ready()
        status = discord.Game('Checking prices')
        await self.change_presence(status=discord.Status.online, activity=status)
        channel = self.get_channel(1074532061223845951)
        while not self.is_closed():
            await channel.typing()
            response = requests.get("http://www.cryptingup.com/api/assets/BTC")
            data = response.json()
            price = data['asset']['quote']['USD']['price']
            # logging.info(f'Requested data:{price}')
            await channel.send(f'Price of BTC: {price}')
            await asyncio.sleep(5)
            # component_logger = logger.getChild('child')
            # component_logger.info('sent')


client = MyClient(intents=discord.Intents.default())
client.run(mytoken.TOKEN)
