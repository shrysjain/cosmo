# Import packages
from dotenv import load_dotenv
import datetime
import requests
import discord
import random
import os

# Load environmental variables
load_dotenv()

token = os.getenv('DISCORD_TOKEN')
nasa_api_key = os.getenv('NASA_API_KEY')
opencage_api_key = os.getenv('OPENCAGE_API_KEY')

# Constants
planets = [
  'mercury',
  'venus',
  'earth',
  'mars',
  'jupiter',
  'saturn',
  'uranus',
  'neptune',
]

space_facts = [
  'The Sun is about 4.6 billion years old and is expected to live another 5 billion years.',
  'Neutron stars can spin at a rate of 600 rotations per second.',
  'The Milky Way galaxy is estimated to contain 100 to 400 billion stars.',
  'The International Space Station travels at a speed of approximately 28,000 kilometers per hour (17,500 miles per hour).',
  'Venus is the hottest planet in our solar system with surface temperatures reaching about 467°C (872°F).',
  'Jupiter\'s Great Red Spot is a giant storm larger than Earth and has been raging for at least 350 years.',
  'A day on Venus (one complete rotation) is longer than a year on Venus (one orbit around the Sun).',
  'Saturn\'s density is so low that it would float in water (if there were a bathtub large enough).',
  'A day on Mars is just slightly longer than a day on Earth, at 24 hours and 37 minutes.',
  'The largest volcano in the solar system is Olympus Mons on Mars, which is about 13.6 miles (22 kilometers) high.',
  'The asteroid belt between Mars and Jupiter is made up of millions of asteroids, but they are spread over a vast distance.',
  'Uranus is the coldest planet in our solar system, with temperatures dropping to as low as -224°C (-371°F).',
  'Halley\'s Comet, visible from Earth approximately every 76 years, last appeared in 1986 and will next appear in 2061.',
  'The dwarf planet Pluto has five known moons: Charon, Styx, Nix, Kerberos, and Hydra.',
  'The Hubble Space Telescope travels at a speed of about 28,000 kilometers per hour (17,500 miles per hour) in low Earth orbit.',
  'The Andromeda Galaxy, our closest neighboring galaxy, is expected to collide with the Milky Way in about 4 billion years.',
  'Black holes are regions of space where gravity is so strong that not even light can escape from them.',
  'A teaspoon of neutron star material would weigh about 6 billion tons.',
  'The Kuiper Belt, beyond Neptune\'s orbit, contains icy bodies and dwarf planets such as Pluto, Haumea, Makemake, and Eris.',
  'There may be a planet made entirely of diamonds, known as 55 Cancri e, located 40 light-years away from Earth.',
  'The Sun makes a complete rotation once approximately every 25-35 days at its equator and around 30 days at its poles.',
  'The cosmic microwave background (CMB) radiation is the afterglow of the Big Bang and fills the universe.',
  'The universe is expanding at an accelerated rate, driven by a mysterious force called dark energy.',
  'The closest black hole to Earth is probably V616 Monocerotis, about 3,000 light-years away in the constellation Monoceros.',
  'The Earth\'s atmosphere extends to about 10,000 kilometers (6,200 miles) above sea level.',
  'The Sun contains more than 99% of the total mass of the entire solar system.',
  'The largest known star, UY Scuti, is over 1,700 times larger in diameter than the Sun.',
  'Mars has the largest volcano and the deepest canyon in the solar system: Olympus Mons and Valles Marineris, respectively.',
  'The Boötes Void is a vast, nearly empty region of space about 250 million light-years in diameter.',
  'The space between stars in the Milky Way is not completely empty but filled with gas and dust.',
  'The moon Io, one of Jupiter\'s moons, is the most volcanically active object in the solar system.',
  'Astronauts on the Moon\'s surface experience about one-sixth of Earth\'s gravity.',
  'Astronomers estimate that the observable universe contains at least 2 trillion galaxies.',
  'The first human-made object to reach space was the Soviet Union\'s Sputnik 1, launched on October 4, 1957.',
  'The nearest galaxy to the Milky Way is the Andromeda Galaxy, about 2.5 million light-years away.',
  'There is a region in space called the "Local Void" where there are very few galaxies.',
  'The light from the Sun takes approximately 8 minutes and 20 seconds to reach Earth.',
  'The largest known galaxy in terms of its physical size is IC 1101, which is about 6 million light-years across.',
  'Astronauts on the International Space Station experience about 16 sunrises and sunsets every day.',
  'The Crab Nebula, a remnant of a supernova explosion, was observed and documented by Chinese astronomers in 1054 AD.',
  'The largest known black hole, TON 618, has a mass estimated to be 66 billion times that of the Sun.',
  'The Perseid meteor shower occurs annually in August when the Earth passes through the debris left by Comet Swift-Tuttle.',
  'The center of the Milky Way galaxy is about 27,000 light-years away from Earth.',
  'The "Pillars of Creation" in the Eagle Nebula are regions of gas and dust where new stars are forming.',
  'A day on Mercury (sunrise to sunrise) is longer than its year (orbit around the Sun) due to its slow rotation.',
  'The Oort Cloud is a hypothesized spherical shell of icy objects surrounding the solar system, about 1 light-year away.',
  'The Voyager 1 spacecraft, launched in 1977, is the farthest human-made object from Earth, currently over 14 billion miles away.',
  'The nearest star system to the Sun is Alpha Centauri, located about 4.37 light-years away.',
  'The space between stars and galaxies is not completely empty but filled with a very low density of particles known as the interstellar medium.',
  'The largest known structure in the universe is the Sloan Great Wall, a vast supercluster of galaxies stretching about 1.38 billion light-years across.'
]

# Create discord client
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'Logged in as {client.user}')
  activity = discord.Activity(type=discord.ActivityType.watching, name="the stars")
  await client.change_presence(activity=activity, status=discord.Status.idle)


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  args = message.content.split(' ')[1:]

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
      ).set_image(url=picture).set_footer(text='Data provided by NASA')
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
    ).set_footer(text='Data provided by SpaceX')
    
    for launch in launches[:5]:
      embed.add_field(
        name=launch['name'],
        value=f'Date: {launch['date_utc'][:10]}\nDetails: {launch.get('details', 'No details available')}',
        inline=False,
      )
        
    await message.reply(embed=embed)
    
  if message.content.startswith('$planet'):
    if len(args) < 1:
      await message.reply(embed=
        discord.Embed(
          title='Invalid Arguments',
          description='Please provide a planet name to get information about in the format `$planet [name]` from the list `mercury, venus, earth, mars, jupiter, saturn, uranus, neptune`.',
          color=0xff0000,
          timestamp=datetime.datetime.now(),
        )
      )
      return
    
    planet = args[0].lower()
    
    if not planet in planets:
      await message.reply(embed=
        discord.Embed(
          title='Invalid Arguments',
          description='Please provide a planet name to get information about in the format `$planet [name]` from the list `mercury, venus, earth, mars, jupiter, saturn, uranus, neptune`.',
          color=0xff0000,
          timestamp=datetime.datetime.now(),
        )
      )
      return
    
    data = requests.get(f'https://api.le-systeme-solaire.net/rest/bodies/{planet}').json()
    
    embed = discord.Embed(
      title=data['englishName'],
      description=f'Here is some information about {data['englishName']}:',
      color=0x00bcff,
      timestamp=datetime.datetime.now()
    ).set_footer(text='Data provided by Le Système Solaire API')
    
    embed.add_field(name='Mass', value=f'{data['mass']['massValue']}*10^{data['mass']['massExponent']} kg')
    embed.add_field(name='Gravity', value=f'{data['gravity']} m/s²')
    embed.add_field(name='Mean Radius', value=f'{data['meanRadius']} km')
    embed.add_field(name='Orbital Period', value=f'{data['sideralOrbit']} days')
    
    await message.reply(embed=embed)
  
  if message.content.startswith('$iss'):
    data = requests.get('http://api.open-notify.org/iss-now.json').json()
    
    position = data['iss_position']
    
    embed = discord.Embed(
      title='ISS Location',
      description='Current position of the International Space Station:',
      color=0x00bcff,
      timestamp=datetime.datetime.now(),
    ).set_footer(text='Data provided by the Open Notify API and the OpenCage Geocoding API')
    
    embed.add_field(name='Latitude', value=position['latitude'])
    embed.add_field(name='Longitude', value=position['longitude'])
    
    latitude = float(position['latitude'])
    longitude = float(position['longitude'])
    
    try:
      location = requests.get(f'https://api.opencagedata.com/geocode/v1/json?q={latitude}+{longitude}&key={opencage_api_key}').json()['results'][0]['formatted']
    except:
      location = 'Unknown Location'
      print('Unable to fetch geocoded location from OpenCage')

    embed.add_field(name='Geocoded Location', value=location, inline=False)
    
    await message.reply(embed=embed)

  if message.content.startswith('$fact'):
    fact = random.choice(space_facts)
    
    embed = discord.Embed(
      title='Random Space Fact',
      description=fact,
      color=0x00bcff,
      timestamp=datetime.datetime.now()
    ).set_footer(text='Data compiled from various sources')
    
    await message.reply(embed=embed)
    
  if message.content.startswith('$marsweather'):
    data = requests.get(f'https://api.nasa.gov/insight_weather/?api_key={nasa_api_key}&feedtype=json&ver=1.0').json()
    
    if 'sol_keys' not in data or len(data['sol_keys']) < 1:
      await message.reply(embed=
        discord.Embed(
          title='Mars Weather Report',
          description='Failed to fetch Mars weather data. Please try again later',
          color=0xff0000,
          timestamp=datetime.datetime.now(),
        )
      )
      return
    
    latest_sol = data['sol_keys'][-1]
    weather = data[latest_sol]
    
    embed = discord.Embed(
      title='Mars Weather Report',
      description=f'Latest weather report from Mars (Sol {latest_sol}):',
      color=0x00bcff,
      timestamp=datetime.datetime.now(),
    ).set_footer(text='Data provided by the NASA InSight API')
    
    embed.add_field(name="Atmospheric Pressure", value=f"{weather['PRE']['av']} Pa")
    embed.add_field(name="Temperature (Average)", value=f"{weather['AT']['av']} °C")
    embed.add_field(name="Wind Speed (Maximum)", value=f"{weather['HWS']['mx']} m/s")
    
    await message.reply(embed=embed)
    
  if message.content.startswith('$asteroid'):
    if len(args) < 1:
      await message.reply(embed=
        discord.Embed(
          title='Invalid Arguments',
          description='Please provide a valid asteroid ID to get information about in the format `$asteroid [id]`.',
          color=0xff0000,
          timestamp=datetime.datetime.now(),
        )
      )
      return
  
    id = args[0]
    
    try:
      data = requests.get(f'https://api.nasa.gov/neo/rest/v1/neo/{id}?api_key={nasa_api_key}').json()
    except :
      await message.reply(embed=
        discord.Embed(
          title='Invalid Arguments',
          description=f'Asteroid with ID `{id}` not found.',
          color=0xff0000,
          timestamp=datetime.datetime.now(),
        )
      )
      return 
    
    if 'error' in data:
      await message.reply(embed=
        discord.Embed(
          title='Invalid Arguments',
          description=f'Asteroid with ID `{id}` not found.',
          color=0xff0000,
          timestamp=datetime.datetime.now(),
        )
      )
      return
    
    embed = discord.Embed(
      title=f'Asteroid Information (ID: {id})',
      description=f"Name: {data['name']}\n"
                  f"NASA JPL URL: {data['nasa_jpl_url']}\n"
                  f"Absolute Magnitude: {data['absolute_magnitude_h']}\n"
                  f"Potentially Hazardous: {'Yes' if data['is_potentially_hazardous_asteroid'] else 'No'}",
      color=0x00bcff,
      timestamp=datetime.datetime.now(),
    ).set_footer(text='Data provided by NASA NeoWs API')
    
    embed.add_field(name="Close Approach Date", value=data['close_approach_data'][0]['close_approach_date'])
    embed.add_field(name="Miss Distance (kilometers)", value=f"{data['close_approach_data'][0]['miss_distance']['kilometers']} km")
    
    await message.reply(embed=embed) 
    
  if message.content.startswith('$constellation'):
    await message.reply(embed=
      discord.Embed(
        title='Command Currently Unavailable',
        description='The `$constellation` command is currently unavailable due to an API outage. Please try again later',
        color=0xff0000,
        timestamp=datetime.datetime.now()
      )
    )
    return
    
    if len(args) < 1:
      await message.reply(embed=
        discord.Embed(
          title='Invalid Arguments',
          description='Please provide a valid constellation name to get information about in the format `$constellation [name]`.',
          color=0xff0000,
          timestamp=datetime.datetime.now(),
        )
      )
      return
  
    id = " ".join(args)
    
    try:
      data = requests.get(f'https://api.le-systeme-solaire.net/rest/bodies/{id.lower()}').json()
    except :
      await message.reply(embed=
        discord.Embed(
          title='Invalid Arguments',
          description=f'Constellation with name `{id}` not found.',
          color=0xff0000,
          timestamp=datetime.datetime.now(),
        )
      )
      return 
    
    if 'error' in data:
      await message.reply(embed=
        discord.Embed(
          title='Invalid Arguments',
          description=f'Constellation with name `{id}` not found.',
          color=0xff0000,
          timestamp=datetime.datetime.now(),
        )
      )
      return
    
    embed = discord.Embed(
      title=f"Constellation Information: {id.capitalize()}",
      description=f"Name: {data['englishName']}\n"
                  f"Constellation Abbreviation: {data['code']}\n"
                  f"Constellation Family: {data['family']}",
      color=0x00bcff,
      timestamp=datetime.datetime.now()
    ).set_footer(text='Data provided by Le Système Solaire API')
    
    await message.reply(embed=embed)
  
client.run(token)
