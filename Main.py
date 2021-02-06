import discord

import datetime

import os
from discord.enums import _is_descriptor

from discord.ext import commands


intent = discord.Intents.all()

client = discord.Client()


@client.event

async def on_ready():
    print(client.user)
    print("봇 준비 완료")
    game = discord.Game("빙산봇 명령어 개발")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event 

async def on_message(message):
    if message.content == "!테스트":
        await message.channel.send("빙산봇은 현재 정상 작동중 입니다 : D")


    if message.content == "!명령어":
        embed = discord.Embed(color=discord.Colour.red(), title="빙산봇 명령어 설명입니다", descriptor="개발중인 명령어도 포함됩니다")
        embed.add_field(name="!테스트", value="빙산봇의 현재상태를 나타냅니다",inline=True)
        embed.add_field(name="!내정보", value="나의 디스코드 정보를 나타냅니다",inline=True)
        embed.set_footer(text="Made By. Sehyun")
        await client.channel.send(embed=embed)






access_token = os.environ["BOT_TOKEN"]
client.run(access_token)


