#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

  # from django.core.management import execute_from_command_line

  print('AQUI')
  import discord
import os
import random

# nix-env -iA nixpkgs.ffmpeg
intents = discord.Intents.default()
intents.typing = True
intents.members = True
client = discord.Client(intents=intents)
token = "OTQyODc0MDYxNzAzMzY0Njk4.Ygq15g.JVVRlByrmqHECtasNq3uWcVOhKo"


rub_text = ['DEMACIAAAAA!!',
            'For Justice.',
            'By bold; be just!',
            'I stand ready.',
            'For Demacia.',
            'To protect our land.']

filename = ['Garen_Original_Move_7.ogg',
            'Garen_Original_Death_1.ogg',
            'Garen_Original_W_5.ogg',
            'Garen_Original_JokeKatarina_1.ogg']

@client.event
async def on_ready():
  print('[READY] user is {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  author = message.author
  guild = message.guild
  voice_client = guild.voice_client

  if message.content.startswith('$disconnect'):
    if voice_client != None:
      print('[DISCONNECTING]')
      await voice_client.disconnect()
    return
  
  roles = author.roles
  for role in roles:
    if role.name == 'Ruven':
      await message.channel.send(random.choice(rub_text))
      
      if author.voice == None:
        return

      channel = author.voice.channel
      if voice_client == None:
        print(f'[CONNECTING] {channel}')
        voice_client = await channel.connect()

       
       
      source = discord.FFmpegOpusAudio(random.choice(filename))
      voice_client.play(source)
      


@client.event
async def on_member_update(before, after):
  print(f'[USER UPDATE] {before.name}')
  print(f'[USER UPDATE] {after.name}')


client.run(token)
    # execute_from_command_line(sys.argv)
