import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import win32com.client as comclt
import configparser
import os
import time

from PIL import ImageGrab
import io

config = configparser.ConfigParser()
config.read("settings.config")

NatroPath = ""

print("NatroAuto")
print("Discord bot by SRP")
print("Natro Macro made by the Natro Team")

if config["SETTINGS"]["NATRO_PATH"] == "None" or "":
    print("WARNING: In the settings file natro path is set to None. With this setting if the macro is closed you can't open it")
else:
    NatroPath = config["SETTINGS"]["NATRO_PATH"]


intents = nextcord.Intents.all()
intents.guild_messages = True
bot = commands.Bot(command_prefix="!", intents=intents)
wsh = comclt.Dispatch("WScript.Shell")


@bot.slash_command(
    name="start",
    description="starts the bot"
)
async def start(interaction: Interaction):
    await interaction.response.defer()


    if not NatroPath == "":
        print("If you have a slow pc and the macro doesn't start up. Its the best to set NATRO_PATH to None")
        os.startfile(NatroPath)
    time.sleep(10)
    wsh.SendKeys("{F1}")
    await interaction.followup.send("Macro started!")



@bot.slash_command(
    name="stop",
    description="stops the bot"
)
async def stop(interaction: Interaction):
    await interaction.response.defer()

    wsh.SendKeys("{F3}")
    os.system("taskkill /F /IM \"RobloxPlayerBeta.exe\"")
    await interaction.followup.send("Macro ended!")



@bot.slash_command(
    name="screenshot",
    description="makes a screenshot of the client"
)
async def screenshot(interaction: Interaction):
    await interaction.response.defer()
    screenshot = ImageGrab.grab()


    image_stream = io.BytesIO()
    screenshot.save(image_stream, format='PNG')
    image_stream.seek(0)

    await interaction.followup.send(file=nextcord.File(image_stream, filename='screenshot.png'))






if not config["SETTINGS"]["BOT_TOKEN"] == "":
    bot.run(config["SETTINGS"]["BOT_TOKEN"])
else:
    print("discord bot token was not found.")
    token = input("If you want to paste it here it will work only this time: ")
    print("Bot will be running soon...")
    bot.run(token)
    



