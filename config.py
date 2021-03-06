import os

class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	APP_ID = int(os.environ.get("APP_ID"))
	API_HASH = os.environ.get("API_HASH")
	DATABASE_URL = os.environ.get("DATABASE_URL")
	SUDO_USERS = list(set(int(x) for x in ''.split()))
	SUDO_USERS.append(853393439)
	SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "[š](https://telegra.ph/file/bd3294484b809258dea27.jpg)) **FORCE SUBSCRIBE :**\n\nForce Group Members To Join A Specific Channel Before Sending Messages in The Group.\nI Will Mute Members if They Not Joined Your Channel And Tell Them To Join The Channel And Unmute Themself By Pressing A Button.",
        
        "[ā](https://telegra.ph/file/bd3294484b809258dea27.jpg) **SETUP :**\n\nFirst Of All Add Me In The Group As Admin With Ban Users Permission And In The Channel As Admin.\nā Note: Only Creator Of The Group Can Setup Me.",
        
        "[ā](https://telegra.ph/file/bd3294484b809258dea27.jpg) **COMMMANDS :**\n\n/ForceSubscribe - To Get The Current Settings.\n/ForceSubscribe no/off/disable - To Turn Of ForceSubscribe.\n/ForceSubscribe {Channel Username} - To Turn On And Setup The Channel.\n/ForceSubscribe clear - To Unmute All Members Who Muted By Me.\n\nā Note: /FSub Is An Alias Of /ForceSubscribe",
        
        "[šØāš»](https://telegra.ph/file/bd3294484b809258dea27.jpg) **DEVELOPED BY @cacell**"
      ]

      START_MSG = "**Hey! [š](https://telegra.ph/file/bd3294484b809258dea27.jpg) [{}](tg://user?id={})**\n\nā I Can Force Members To Join A Specific Channel Before Writing Messages In The Group.\nā Learn More At š /help"
