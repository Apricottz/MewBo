import discord
from discord.ext import commands
import random

import Affects

TOKEN = 'MTEyNjEzMzQwMDI0ODUzMzA4Mw.G7N62t.uJDnFxSAqQ7kKyTyl8750gVECmFss261M3-Wkc'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
	print(f'Logged in as {bot.user.name}')


# @bot.command()
# async def ping( ctx ):
# 	await ctx.send('Pong!')


# @bot.command()
# async def catch( ctx ):
# 	pokemon_list = ['Pikachu', 'Charmander', 'Bulbasaur', 'Squirtle', 'Jigglypuff']
# 	caught_pokemon = random.choice(pokemon_list)
# 	await ctx.send(f'You caught a wild {caught_pokemon}!')


# @bot.command()
# async def info1( ctx, pokemon ):
# 	# Implement your code to retrieve information about the given Pokémon
# 	# This could involve making API calls to a Pokémon data source
# 	await ctx.send(f'Information about {pokemon}')


@bot.command()
async def resist( ctx, pokemon ):
	# pokemon.capitalize()
	for i in Affects.data:
		if pokemon.capitalize() == i["pokemon_name"]:
			if len(i["resistance"].keys()) > 1:
				x = list(i["resistance"]["62.5"])
				y = list(i["resistance"]["39"])
				await ctx.send(f"{', '.join(x)}:\nDamage multiplier = {0.625}\n\n{', '.join(y)}:\nDamage multiplier = {0.39}")
			elif len(i["resistance"].keys()) == 1 and "62.5" in i["resistance"]:
				x = list(i["resistance"]["62.5"])
				await ctx.send(f"{', '.join(x)}:\nDamage multiplier = {0.625}")
			else:
				# len(i["resistance"].keys()) == 1 and i["resistance"]["39"]:
				x = list(i["resistance"]["39"])
				await ctx.send(f"{', '.join(x)}:\nDamage = {0.39}")


@bot.command()
async def weak( ctx, pokemon ):
	# pokemon.capitalize()
	for i in Affects.data:
		if pokemon.capitalize() == i["pokemon_name"]:
			if len(i["weakness"].keys()) > 1:
				x = i["weakness"]["160"]
				y = i["weakness"]["256"]
				await ctx.send(f"{list(x)}: Damage multiplier = {1.60}\n{list(y)}: Damage multiplier = {2.56}")
			elif len(i["weakness"].keys()) == 1 and "160" in i["weakness"]:
				x = i["weakness"]["160"]
				await ctx.send(f"{list(x)}: Damage multiplier = {1.6}")
			else:
				x = i["weakness"]["256"]
				await ctx.send(f"{list(x)}: Damage multiplier = {2.56}")

bot.run("MTEyNjEzMzQwMDI0ODUzMzA4Mw.G7N62t.uJDnFxSAqQ7kKyTyl8750gVECmFss261M3-Wkc")
