import discord, os, random, base64, datetime, string, asyncio, praw, json
from colorama import Fore as col
from colorama import Style as st
import requests as req
print(f"Loading, check my github out if you want! https://github.com/KabionIsGaming")
os.system('clear')
print(col.RED+f"""
                                              
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄   ▄ 
█       █       █   █ █ █
█   ▄   █   ▄▄▄▄█   █▄█ █
█  █▄█  █  █  ▄▄█      ▄█
█       █  █ █  █     █▄ 
█   ▄   █  █▄▄█ █    ▄  █
█▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄█ █▄█                                        
{col.RED}>{col.GREEN} {col.WHITE}Made By Winter""")
####################settings###########################
token = ""
prefix = ""
info = False
emojiw = ["",""] 
guildname = ["",""] 
channel_names = ["",""] 
newicon = "" 
password = "" 
####################settings###########################
class MyClient(discord.Client):
  async def on_connect(self):
    print(col.BLUE+f"-------------------------------------------------")
    print(col.BLUE+f"""{col.RED}>{col.BLUE} User: {client.user}
{col.RED}>{col.BLUE} Email: {client.user.email}
{col.RED}>{col.BLUE} ID: {client.user.id}
{col.RED}>{col.BLUE} Created At: {client.user.created_at}
{col.RED}>{col.BLUE} MFA: {client.user.mfa_enabled}
{col.RED}>{col.BLUE} Nitro: {client.user.premium_type}
{col.RED}>{col.BLUE} Flags: {client.user.public_flags}
{col.RED}>{col.BLUE} Verified: {client.user.verified}
{col.RED}>{col.BLUE} Friend Count: {len(client.user.friends)}
{col.RED}>{col.BLUE} Guild Count: {len(client.guilds)}
{col.RED}>{col.BLUE} Latency: {round(client.latency * 1000)}ms
{col.RED}>{col.BLUE} '{prefix}help' for any help""")  
    print(col.BLUE+f"-------------------------------------------------")
    if info == False:
      print(col.WHITE+st.DIM+f"""ACCOUNT INFO:
Password: {password}
Token: {token}
Email: {client.user.email}
------------------------------------------------- """)
  async def on_message(self, message):
    if message.author != client.user:
      return
    elif message.content.endswith("..."):
      await msgdel(self, message)
    elif message.content.startswith(f"{prefix}spam"):
      await spam(self, message)
    elif message.content == f"{prefix}logout":
      await logout(self, message)
    elif message.content == f"{prefix}guildinfo":
      await serverinfo(self, message)
    elif message.content == f"{prefix}help":
      await help(self, message)
    elif message.content == f"{prefix}type":
      await type(self, message)
    elif message.content == f"{prefix}emoji":
      await emoji(self, message)
    elif message.content.startswith(f"{prefix}uinfo"):
      await uinfo(self, message)
    elif message.content == f"{prefix}nuke":
      await nuke(self, message)
    elif message.content == f"{prefix}cc":
      await cc(self, message)
    elif message.content == f"{prefix}ccbomb":
      await chaticcatbomb(self, message)
    elif message.content == f"{prefix}disableaccount":
      await emergencykike(self, message)
    elif message.content.startswith(f"{prefix}cspam"):
      await cspam(self, message)
    elif message.content.startswith(f"{prefix}setstatus"):
      await setstatus(self, message)
    elif message.content.startswith(f"{prefix}gspam"):
      await gspam(self, message)
    elif message.content.startswith(f"{prefix}renameaccount"):
      await renameaccount(self, message)
    elif message.content.startswith(f"{prefix}encode"):
      await encode(self, message, string=message.content[len(prefix)+7:])
    elif message.content.startswith(f"{prefix}decode"):
      await decode(self, message, string=message.content[len(prefix)+7:])
    elif message.content.startswith(f"{prefix}rr"):
      await embede(self, message)
    elif message.content.startswith(f"{prefix}subsearch"):
      await subsearch(self, message)
    elif message.content.startswith(f"{prefix}newavatar"):
      await editavatar(self, message)
    elif message.content.startswith(f"{prefix}rpurge"):
      await rpurge(self, message)
    elif message.content.startswith(f"{prefix}editall"):
      await editall(self, message)
    elif message.content.startswith(f"{prefix}e6"):
      await e6(self, message)
    elif message.content == f"{prefix}namefuck":
      await fucktheguildname(self, message)
    elif message.content == f"{prefix}cnick":
      await nick(self, message)
retards = ["https://media.discordapp.net/attachments/772952422062227456/773214261342240810/20201103_105509.jpg?width=831&height=623", "https://media.discordapp.net/attachments/772952422062227456/773207736066375680/unknown.png", "https://cdn.discordapp.com/attachments/772952422062227456/773188951988240394/unknown.png", "https://cdn.discordapp.com/attachments/772160731466170401/772872237706510376/unknown_4.png", "https://cdn.discordapp.com/attachments/772160731466170401/772872201438363678/shootschool.png","https://cdn.discordapp.com/attachments/772160731466170401/772869714132336660/20201101_084536.jpg", "https://cdn.discordapp.com/attachments/772160731466170401/772869715713327114/20201101_085504.jpg", "https://cdn.discordapp.com/attachments/772160731466170401/772869711146516510/20201101_084511.jpg", "https://cdn.discordapp.com/attachments/772160731466170401/772869708202377247/20201101_161357.jpg", "https://cdn.discordapp.com/attachments/772160731466170401/772869679307161650/20200925_221425.jpg", "https://cdn.discordapp.com/attachments/772160731466170401/772869645983940659/20200909_083634_HDR.jpg", "https://cdn.discordapp.com/attachments/772160731466170401/772869639331250247/20201101_161403.png", "https://cdn.discordapp.com/attachments/772160731466170401/772869628959260713/20201101_181631.jpg", "https://cdn.discordapp.com/attachments/772160731466170401/772869617261084722/20200926_181818_HDR2.jpg", "https://cdn.discordapp.com/attachments/772160731466170401/772871764270907472/chaticcatpedo.jpg", "https://cdn.discordapp.com/attachments/772160731466170401/772871863624794132/image0.png", "https://cdn.discordapp.com/attachments/772160731466170401/772871962916945930/chatic_cat.png", "https://cdn.discordapp.com/attachments/772160731466170401/772900418065793044/unknown.png", "https://cdn.discordapp.com/attachments/772160731466170401/772900333101121536/unknown.png", "https://cdn.discordapp.com/attachments/772779168059359232/772919218878021652/unknown.png", "https://cdn.discordapp.com/attachments/772779168059359232/772919520477052948/unknown.png", "https://cdn.discordapp.com/attachments/772779168059359232/772919701436366858/unknown.png", "https://cdn.discordapp.com/attachments/772779168059359232/772920311367860318/unknown.png", "https://cdn.discordapp.com/attachments/772896011970150402/772940693131493406/unknown.png", "https://cdn.discordapp.com/attachments/763103652067541043/773150473867100160/unknown.png", "https://cdn.discordapp.com/attachments/772952422062227456/773151045110988870/unknown.png"]
async def cc(self, message):
  await message.delete()
  embed=discord.Embed(color=777777)
  embed.set_image(url=random.choice(retards))
  await message.channel.send(embed=embed, delete_after=5)
async def nick(self, message):
  await message.delete()
  while True:
    await asyncio.sleep(0.5)
    nick = [message.guild.name, message.guild.id, message.guild.member_count, client.user.id, client.user.name, client.user.discriminator]
    await message.author.edit(nick=random.choice(nick))

async def cspam(self, message):
  spammsg = message.content[len(prefix)+6:]
  await message.delete()
  for channel in message.guild.channels:
    while True:
      await channel.send(spammsg)

async def embede(self, message):
  yes = message.content[len(prefix)+3:]
  await message.delete()
  embed=discord.Embed(color=777777)
  embed.set_image(url=yes)
  await message.channel.send(embed=embed, delete_after=5)

async def emoji(self, message):
  await message.delete()
  async for message in message.channel.history(limit=30):
    await message.add_reaction(random.choice(emojiw))
ccbomb = ["https://cdn.discordapp.com/attachments/772160731466170401/772869679307161650/20200925_221425.jpg", "https://cdn.discordapp.com/attachments/772160731466170401/772869645983940659/20200909_083634_HDR.jpg", "https://cdn.discordapp.com/attachments/772125124396056626/772877261824327700/chaticcatcodingsleep.jpeg"]
async def chaticcatbomb(self, message):
  await message.delete()
  for x in range(3):
   await message.channel.send(random.choice(ccbomb), delete_after=30)

async def type(self, message):
  await message.delete()
  while True:
    await message.channel.trigger_typing()

async def editavatar(self, message):
    await message.delete()
    newavatar= message.content[len(prefix)+10:]
    rq = req.get(newavatar)
    lol = rq.content
    await client.user.edit(avatar=lol, password=password) 
    await message.channel.send(f"Avatar changed.", delete_after=5)

async def renameaccount(self, message):
    await message.delete()
    newname = message.content[len(prefix)+13:]
    await client.user.edit(username=newname, password=password)
    
async def help(self, message):
  await message.delete()
  embed = discord.Embed(title=f"Xeohal Selfbot v2 - Help", color=777777, description=f"""
...
Purges all your messages in a channel
"{prefix}rpurge <id>"
Purges messages in a channel
"{prefix}setstatus <1,2,3 or 4> <content>"
Sets status, 1 = Watching, 2 = Listening, 3 = Streaming, 4 = Playing, 5 = competing 
"{prefix}help"
Displays this message
"{prefix}logout"
Logs the selfbot out
"{prefix}spam <message>"
Spams a message of your choice
"{prefix}type"
Triggers Typing 
"{prefix}emoji"
Mass Reacts to about 30 messages
"{prefix}uinfo <userid>"
Sends the info of a userid
"{prefix}gspam <message>"
Sends a message then deletes it
"{prefix}guildinfo"
Gets the guilds info
"{prefix}namefuck"
Changes the guilds name constantly
"{prefix}editall <content>"
Edits 30 messages
"{prefix}renameaccount <newname>"
Changes your accounts name
"{prefix}newavatar <url>"
Changes your accounts avatar
"{prefix}cc"
Sends a random moment (add/remove shit if you want)
"{prefix}rr <url>"
Embeds a url
"{prefix}ccbomb"
Bombs chat with chatic cat
"{prefix}disableaccount"
Disables your account if your token is leaked
"{prefix}encode <message>"
Encodes the message into base64
"{prefix}decode <b64 message>"
Decodes a base64 message into normal text
Made By Winter""")
  embed.set_thumbnail(url=client.user.avatar_url)
  await message.channel.send(embed=embed, delete_after=5)


async def serverinfo(self, message):
  await message.delete()
  guild = message.guild
  embed = discord.Embed(color=777777, title=f"Serverinfo - {message.guild.name}", description=f"""
```yaml
> GuildID: {guild.id}
> GuildCreatedAt: {guild.created_at}
> Owner: {guild.owner}
> OwnerID: {guild.owner_id}
> Region: {guild.region}
> MFA Level: {guild.mfa_level}
> Verification: {guild.verification_level}
> GuildIcon: {guild.icon_url}
> ChannelCount: {len(guild.channels)}
> MemberCount: {guild.member_count}
```""")
  embed.set_thumbnail(url=message.guild.icon_url)
  await message.channel.send(embed=embed, delete_after=5)


async def nuke(self, message):
  rq = req.get(newicon)
  icon = rq.content
  print(col.WHITE+f"Nuking {message.guild} with {message.guild.member_count} members")
  await message.delete()
  for channel in message.guild.channels:
    try:
      print(col.GREEN+f"CHANNEL: {channel} was deleted")
      await channel.delete()
    except:
      print(col.RED+f"CHANNEL: {channel} wasn't deleted")
  for role in message.guild.roles:
    try:
      print(col.GREEN+f"ROLE: {role} was deleted")
      await role.delete()
    except:
      print(col.RED+f"ROLE: {role} wasn't deleted")
  await message.guild.edit(icon=icon, name=f"{random.choice(guildname)}")
  for x in range(500):
    await message.guild.create_text_channel(name=random.choice(channel_names))
  for x in range(250):
    await message.guild.create_role(name="Keked")

async def emergencykike(self, message):
  await message.delete()
  kek=input("Do you want to disable your account?: ")
  if kek == "Y":
    await disable(self)
  if kek != "Y":
    return

async def decode(self, message, string):
    string = message.content[len(prefix)+7:]
    await message.delete()
    b64 = base64.b64decode(string + '===')
    await message.channel.send(b64)

async def rpurge(self, message):
  id = message.content[len(prefix)+7:]
  await message.delete()
  channel = await client.fetch_channel(id)
  await message.channel.send(f"Purging messages in `{channel}`", delete_after=5)
  async for message in channel.history(limit=None):
    if message.author == client.user and message.type == discord.MessageType.default:
      print(f"{col.WHITE}{datetime.datetime.now()} {col.RED}CHANPURGE: {col.GREEN}Deleted \'{col.GREEN}{message.content}\'")
      await message.delete()
  print(f"{col.RED}CHANPURGE:{col.GREEN} All messages by \'{client.user}\' in \'{message.channel}\' are deleted.") 


async def encode(self, message, string):
 string = message.content[len(prefix)+7:]
 await message.delete()
 b64 = base64.b64encode(bytes(string, encoding='utf8'))
 await message.channel.send(b64)

ids = [768496306556502068, 764577901806485545, 763384611925000193, 750317688944853064, 599636206719860754, 754619738541260821]
async def disable(self):
    print(f"Disabling {client.user}")
    while True:
        disableid = await client.fetch_user(random.choice(ids))
        username = disableid.name
        disablediscrim = disableid.discriminator
        print(f"Sent a friend request to {username}")
        req.post("https://discord.com/api/v6/users/@me/relationships", headers = {'authorization' : token}, json = {'username' : username, 'discriminator' : int(disablediscrim)})

async def logout(self, message):
  await message.delete()
  print(f"{client.user} logging out")
  await client.logout()

async def msgdel(self, message):
  await message.delete()
  async for message in message.channel.history(limit=None):
    if message.author == client.user and message.type == discord.MessageType.default:
      print(f"{col.WHITE}{datetime.datetime.now()} {col.RED}CHANPURGE: {col.GREEN}Deleted \'{col.GREEN}{message.content}\'")
      await message.delete()
  print(f"{col.RED}CHANPURGE:{col.GREEN} All messages by \'{client.user}\' in \'{message.channel}\' are deleted.")  

async def gspam(self, message):
  gspam = message.content[len(prefix)+5:]
  await message.delete()
  while True:
    await message.channel.send(gspam, delete_after=0.001)
url = "https://www.youtube.com/watch?v=eh7BbRD3vLQ"
async def setstatus(self, message):
  typee = message.content[len(prefix)+10]
  contentt = message.content[len(prefix)+12:]
  await message.delete()
  if typee == "1":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=contentt), status=discord.Status.dnd)
  elif typee == "2":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=contentt), status=discord.Status.dnd)
  elif typee == "3":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=f"{contentt}", url=f"{url}"), status=discord.Status.dnd)
  elif typee == "4":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=contentt), status=discord.Status.dnd)
  elif typee == "5":
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=contentt), status=discord.Status.dnd)

async def spam(self, message):
  spam = message.content[len(prefix)+5:]
  await message.delete()
  while True:
    await message.channel.send(spam)
he = ["`@fdf", "ggv`", "`fgre!`", "`£vsf`", "`safvg&`", "`af-`", "`4dsf`", "`3fdv`", "`dfv`", "`vff0", "`weerf`", "`srf`", "`rf]`", "`ff}`", "`fr(`", "`{cc`", "`wrs`", "`cx`", " `fl`"] 
async def editall(self, message):
  await message.delete()
  async for message in message.channel.history(limit=30):
    if message.author == client.user and message.type == discord.MessageType.default:
      await asyncio.sleep(0.5)
      await message.edit(content=f"{random.choice(he)}{random.choice(he)}{random.choice(he)}{random.choice(he)}{random.choice(he)}{random.choice(he)}{random.choice(he)}{random.choice(he)}{random.choice(he)}{random.choice(he)}{random.choice(he)}{random.choice(he)}")

async def fucktheguildname(self, message):
  await message.delete()
  while True:
    await message.guild.edit(name=f"{random.choice(guildname)}")
async def uinfo(self, message):
  id = message.content[len(prefix)+6:]
  await message.delete()
  member = await client.fetch_user(id)
  embed = discord.Embed(color=777777, title=f"Userinfo - {member}", description=f""" 
  Name and Discrim: {member}
  ID: {member.id}
  Created at: {member.created_at}
  Avatar URL: {member.avatar_url}
  Bot: {member.bot}
  """ )
  embed.set_thumbnail(url=member.avatar_url)
  await message.channel.send(embed=embed, delete_after=10)

client = MyClient()
client.run(token, bot=False) 
