import os
import discord
from dotenv import load_dotenv
import csv
import string

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
text_file_by_rogue = 'songs_by_rogue.txt'

client = discord.Client()

def get_songs():
    song_text = ''
    with open(text_file_by_rogue, 'r') as file:
        all_songs = file.readlines()
        for song in all_songs:
            song_text = song_text  + song + '\n'
    return song_text


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print('{} is connected to the following guild:\n{} (id: {})'.format(client.user, guild.name, guild.id))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #if message.channel != 'bot_testing_ground':
    #    return
    content = message.content
    content = content.lower()
    sender = str(message.author)

    print(content, ' || ', sender)

    if content.startswith('!bot'):
        await message.channel.send('Not Case Sensitive ;)\n!Links\n!Spotify\n!YouTube\n!Twitter\n!Instagram\n!Twitch\n!About\n!Songs')

    elif content.startswith('!links'):
        await message.channel.send('Spotify: https://spoti.fi/3dzwOds\nYouTube: https://bit.ly/2DxUcLz\nTwitter: https://twitter.com/soundsbyrogue\nInstagram: https://www.instagram.com/soundsbyrogue/\nTwitch: https://twitch.tv/soundsbyrogue')

    elif content.startswith('!spotify'):
        await message.channel.send('Spotify: https://spoti.fi/3dzwOds')

    elif content.startswith('!youtube'):
        await message.channel.send('YouTube: https://bit.ly/2DxUcLz')

    elif content.startswith('!twitter'):
        await message.channel.send('Twitter: https://twitter.com/soundsbyrogue')

    elif content.startswith('!instagram'):
        await message.channel.send('Instagram: https://www.instagram.com/soundsbyrogue/')

    elif content.startswith('!twitch'):
        await message.channel.send('Twitch: https://twitch.tv/soundsbyrogue')

    elif content.startswith('!songs'):
        song_text = get_songs()
        await message.channel.send('Songs by Rogue:\n__________\n{}'.format(song_text))

    elif content.startswith('!update '):
        if sender == 'RogueAnathema#1420' or sender == 'Jtriley15#6248':
            song = content.replace('!update ','')
            song = string.capwords(song)
            with open(text_file_by_rogue, 'a') as file:
                line = song + '\n'
                file.write(line)
            song_text = get_songs()
            await message.channel.send('Songs updated, new list:\n__________\n{}'.format(song_text))

    elif content.startswith('!remove '):
        if sender == 'RogueAnathema#1420' or sender == 'Jtriley15#6248':
            song = content.replace('!remove ','')
            song = string.capwords(song)
            with open(text_file_by_rogue, 'r') as file:
                lines = file.readlines()
            with open(text_file_by_rogue, 'w') as file:
                for line in lines:
                    if line.strip('\n') != song:
                        file.write(line)
            song_text = get_songs()
            await message.channel.send('Songs updated, new list:\n__________\n{}'.format(song_text))

    elif content.startswith('!analytics'):
        if sender == 'RogueAnathema#1420' or sender == 'Jtriley15#6248':
            await message.channel.send('Analytics soon too come :)')

client.run(TOKEN)