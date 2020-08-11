import discord
import time
import requests
import validators
from random import randint

client = discord.Client()

TOKEN = "<Insert Token Here>"

MUSIC_COMMANDS = ('-p', '-n', '-seek', '-q', '!p', '!s', '!fs', '!seek', '!q', '!leave', '!clear', '!skipto')
MUSIC_REQUESTS_CHANNEL_ID = 718229417410953248 
MEMES_CHANNEL_ID = 719514778040795136
HANGOUTS_CHANNEL_ID = 273374818882289664
ALLOWED_IMAGE_FORMATS = ["image/gif", "image/png", "image/jpeg", "image/jpg", "image/tiff", "image/heic", "image/heif"]

THRESHOLD = 70

SPECIFICS = {
    "Sylar#4612": "Yes, this is me",            # Илиян
    "GR1M#4043": "Освен един CS да напрайм?",   # Димитър
    "batkolyo#6770": "Помниш ли, помниш ли",    # Николай
    "Des#8568": "Ти няма ли да си лягаш?",      # Георги
    "sslavov93#1485": "Ай стига радиация!",     # Светльо
    "?kr#8843": "Въй, кво щи пусна!",           # Красимир
    "ageyne#9358": "Ае къде са е?",             # Сашето
    "Nyxi4#7826": "Ти шкембе ядеш ли?",         # Никола
    "Teo#7477": "Браво беее.",                  # Тео
    "Fwank#2628": "Малка, баце.",               # Тинчев
    "taratora#3531": "Момчета, гаси играта."    # Венци
}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(MUSIC_COMMANDS):
        if message.channel.id != MUSIC_REQUESTS_CHANNEL_ID:            
            autoresponse = await message.channel.send('{}, please use #music-requests'.format(message.author.mention))
            time.sleep(10)
            await autoresponse.delete()
            await message.delete()

    elif message.channel.id == MEMES_CHANNEL_ID:
        if not validators.url(message.content) and len(message.attachments) <= 0:
            await message.delete()
            return

        r = requests.head(message.content)
        if r.headers['content-type'] not in ALLOWED_IMAGE_FORMATS: 
            await message.delete()
    
    elif message.channel.id == HANGOUTS_CHANNEL_ID:
        if randint(1, 101) >= THRESHOLD:    
            hangouts = client.get_channel(HANGOUTS_CHANNEL_ID)
            member = hangouts.members[randint(0, len(hangouts.members) - 1)]

            if SPECIFICS.get(str(member), ""):
                # print(f'{SPECIFICS[str(member)]} - {str(member.name)}')
                await hangouts.send(f'{SPECIFICS[str(member)]} - {str(member.name)}')

client.run(TOKEN)

