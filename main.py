from email import message
from tokenize import Token
import discord
import os
from discord.ext import commands
import json
import random

## setando prefixo do bot e permissões.
client = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , case_insensitive=True)

## carregando os comandos
with open('config.json') as f:
    config = json.load(f)
    TOKEN = config['TOKEN']
    prefixo = config['prefix']
    owner_id = config['owner_id']
    

## ao logar o bot:
@client.event
async def on_ready():
  print('Bot monitor está online! ✅, com o nome "{0.user}"'.format(client))

async def on_message(message):
  if message.author == client.user:
    return

## hello
@client.command()
async def ola(ctx):
  await ctx.send(f"Olá, @{ctx.author} tudo bem?")

## mensagemm privada, ctx.author.send('mensagem')
@client.command()
async def ajuda(ctx):
    await ctx.author.send(f"Olá {ctx.author}, tudo bem? como poderia ajudar?")

## verificar se é monitor.
@client.command()
async def adm(ctx):
    if ctx.author.id == owner_id:
          await ctx.send(f"Olá, {ctx.author} você é monitor!  👨🏻‍💻✅")
    else:
          await ctx.send(f"Olá, {ctx.author} você não é monitor! 👨🏻‍💻❌")

## !clear
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
 
## !kick @user
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.id == owner_id:
        await member.kick(reason=reason)
        await ctx.send(f'{member} foi kickado com sucesso!')
    else:
        await ctx.send(f'Você não tem permissão para kickar membros!')

## !ban @user
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.id == owner_id:
        await member.ban(reason=reason)
        await ctx.send(f'{member} foi banido com sucesso!')
    else:
        await ctx.send(f'Você não tem permissão para banir membros!')      

## !unban @user
@client.command()
async def unban(ctx, *, member):
    if ctx.author.id == owner_id:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} foi desbanido com sucesso!')
                return
    else:
        await ctx.send(f'Você não tem permissão para desbanir membros!')


## !ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)}ms')

## client.run(os.getenv('TOKEN'))
client.run(TOKEN)