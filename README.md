# Cosmo 🚀

Cosmo is a versatile Discord bot designed for astronomy enthusiasts and learners. It provides real-time information about celestial objects and bodies, satellites and stations, and space facts. With commands powered by various APIs, Cosmo enriches your Discord server with educational content and interactive features related to space exploration.

## Commands

- `$ping`: Displays the bot's roundtrip latency.
- `$apod`: Displays the Astronomy Picture of the Day from NASA.
- `$launches`: Fetches upcoming rocket launches from the SpaceX API.
- `$planet [name]`: Provides details about a specific planet in our solar system.
- `$iss`: Retrieves current position and details of the International Space Station.
- `$fact`: Shares interesting space facts.
- `$constellation [name]`: Shows information about a specific constellation.
- `$asteroid [id]`: Displays information about a specific asteroid.
- `$marsweather`: Displays information about the current weather on Mars.
- `$exoplanet [name]`: Shows information about a specific exoplanet.
- `$spacequiz$`: Quizzes your knowledge on some fun space trivia.
- `$help`: Displays an informative preview of all available commands.

## Built With

- Discord.py
- NASA API
- SpaceX API
- Le Système Solaire API
- OpenCage Geocoding API
- Open Notify API
- Caltech IPAC

## Getting Started

### Add Cosmo to Your Server (RECOMMENDED)

To add Cosmo to your Discord server, click [here](https://discord.com/oauth2/authorize?client_id=1257118234587430983&permissions=68608&integration_type=0&scope=bot) and authorize the bot to join your server with appropriate permissions.

### Self-Hosting

To self-host Cosmo on your own server:

1. Clone or download this repository

```bash
git clone https://github.com/shrysjain/cosmo.git
cd cosmo
```

*Alternatively, clone via SSH, the GitHub CLI, or GitHub desktop*

2. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

3. Create a Discord bot application in the Discord developers portal with the `message_content` intent.

4. Create a `.env` file in the project root directory and add your Discord bot token, NASA API key, and OpenCage API key:

```env
DISCORD_TOKEN=
NASA_API_KEY=
OPENCAGE_API_KEY=
```

5. Run the bot:

```bash
python3 main.py
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Licensing

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
