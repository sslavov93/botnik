import discord

client = discord.Client()

MUSIC_COMMANDS = ('-', '*')
MUSIC_REQUESTS_CHANNEL_ID = 718229417410953248 


@client.event
async def on_ready():
    # Remove this 
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    

    if message.content.startswith(MUSIC_COMMANDS):
        if message.channel.id != MUSIC_REQUESTS_CHANNEL_ID:            
            await message.channel.send('Not the correct channel. Let me fix that for you.')
            
            for each in client.get_all_channels():
                if type(each) == discord.channel.VoiceChannel and message.author in each.members:
                    print(each.name)
                    await each.connect()
                    
                    music_channel = client.get_channel(MUSIC_REQUESTS_CHANNEL_ID) 
                    await music_channel.send(message.content)
                    print(client.voice_clients) 
                    await each.leave()
            

# TODO export in file
client.run('')
