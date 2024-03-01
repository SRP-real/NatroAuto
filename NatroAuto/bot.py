import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import win32com.client as comclt
import configparser
import os
import time
import pyautogui

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
async def start(interaction: Interaction):
    await interaction.response.defer()

    wsh.SendKeys("{F3}")
    os.system("taskkill /F /IM \"RobloxPlayerBeta.exe\"")
    await interaction.followup.send("Macro ended!")












bot.run(config["SETTINGS"]["BOT_TOKEN"])
