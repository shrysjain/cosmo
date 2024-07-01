# Import packages
from dotenv import load_dotenv
import datetime
import discord
import requests
import os

# Load environmental variables
load_dotenv()

token = os.getenv('DISCORD_TOKEN')
nasa_api_key = os.getenv('NASA_API_KEY')

# Create discord client
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  args = message.split(" ")[1:]

  if message.content.startswith('$ping'):
    await message.reply(embed=
      discord.Embed(
        title='Pong!',
        description=f'Roundtrip latency is **{round(1000 * client.latency)}ms** 🏓',
        color=0x00bcff,
        timestamp=datetime.datetime.now(),
      )
    )
    
  if message.content.startswith('$apod'):
    picture = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}').json()['url']
    
    await message.reply(embed=
      discord.Embed(
        title='Astronomy Picture of the Day',
        color=0x00bcff,
        timestamp=datetime.datetime.now(),
      ).set_image(url=picture).set_footer(text='Astronomy Picture of the Day provided by NASA')
    )
    
  if message.content.startswith('$launches'):
    launches = requests.get('https://api.spacexdata.com/v4/launches/upcoming').json()
    
    if not launches:
      await message.reply(embed=
        discord.Embed(
          title='Upcoming Launches',
          description='Failed to retrieve data or no upcoming launches',
          color=0xff0000,
          timestamp=datetime.datetime.now()
        )
      )
      return
    
    embed = discord.Embed(
      title='Upcoming Launches',
      color=0x00bcff,
      timestamp=datetime.datetime.now()
    ).set_footer(text='Upcoming launch data provided by SpaceX')
    
    for launch in launches[:5]:
      embed.add_field(
        name=launch['name'],
        value=f'Date: {launch['date_utc'][:10]}\nDetails: {launch.get('details', 'No details available')}',
        inline=False,
      )
        
    await message.reply(embed=embed)
    
  # if message.content.startswith('$planet'):
  #   if len(args) < 1:
  #     await message.reply('Please provide a planet name to get information about in the format `$planet [name]`')
  #     return

client.run(token)
