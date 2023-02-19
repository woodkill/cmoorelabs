import discord
from discord.ext import commands

class Select(discord.ui.Select):

    def __init__(self):
        options = [
            discord.SelectOption(label="Blue", emoji="🟦", description="Blue role"),
            discord.SelectOption(label="Red", emoji="🟥", description="Red role"),
            discord.SelectOption(label="Yellow", emoji="🟨", description="Yellow role")
        ]
        super().__init__(placeholder="Choose your team", max_values=1, min_values=1, options=options)
        async def callback(self, interaction: discord.Interaction):
            user = interaction.user
            guild = interaction.guild
            if self.value[0] == "Blue":
                role = await guild.create_role(name="Blue", color=discord.Color.blue())
                await user.edit(roles=[role])
                await interaction.response.send_message("Team Blue", ephemeral=True)
            elif self.value[0] == "Red":
                role = await guild.create_role(name="Red", color=discord.Color.red())
                await user.edit(roles=[role])
                await interaction.response.send_message("Team Red", ephemeral=False)
            elif self.value[0] == "Yellow":
                role = await guild.create_role(name="Yellow", color=discord.Color.yellow())
                await user.edit(roles=[role])
                await interaction.response.send_message("Team Yellow", ephemeral=False)

class SelectView(discord.ui.View):

    def __init__(self, *, timeout=30):