import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import qrcode
import io

# Load environment  variables from .env file 

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

# Define bot intents (permissions) 

intents = discord.Intents.all()

intents.messages = True

intents.members = True

# Initialize bot with command prefix '!'

bot = commands.Bot(command_prefix= '!', intents =intents)

# Bot Commands

@bot.command() 
async def info(ctx):
    """Simple command to display bot authorship. """

    await ctx.send('I am a bot developed by Alvaro! ')

@bot.command()
async def crypto(ctx, coin: str):
    """
    Queries the CoinGecko API to fetch the real-time USD price
    of the requested cryptocurrency.
    """
    try:
        coin = coin.lower().strip()
        response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd')
        data = response.json()

        if coin in data:
            price = data[coin]['usd']
            await ctx.send(f'the price of  {coin} is ${price} USD')
        else:
            await ctx.send('Cryptocurrency not found.')

    except Exception as e:
        await ctx.send('An error occurred while fetching the crypto price.')
        print(e)

@bot.command()
async def news(ctx):
    """
    Fetches the top 3 tech stories from HackerNews and displays them.

    """
    try:
        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        response = requests.get(top_stories_url)
        story_ids = response.json()

        message_text = "** Top 3 Tech Stories - HackerNews:**\n"


        for index, story_id in enumerate(story_ids[:3], 1):
            item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            item_res = requests.get(item_url)
            item_data = item_res.json()

            if item_data and 'title' in item_data and 'url' in item_data:
                title = item_data['title']
                url = item_data['url']
                score = item_data.get('score' , 0)

                message_text += f"\n{index}. ⭐ **{score} pts** - [{title}]({url})"

        await ctx.send(message_text)


    except Exception as e:

        await ctx.send('An error occurred while fetching the news.')
        print(e)
                  
             

@bot.command()
async def qr(ctx, *, text: str):

    """
    Generates and sends a QR code image based on the provided text or URL
    using an in-memory buffer.
    """

    try:
        img = qrcode.make(text)

        buffer = io.BytesIO()

        img.save(buffer, format = 'PNG')

        buffer.seek(0)

        file = discord.File(buffer,filename='qrcode.png')
        await ctx.send(f"QR code generated:", file=file)

    except Exception as ex:
        await ctx.send('An error occurred while generating the QR code.')
        print(ex)



# Bot Events
@bot.event
async def on_message(message):
    """Listens  to all messages to handle auto-replies."""
    if message.author == bot.user:
        return
    if 'hola'   in message.content.lower() or 'hello' in message.content.lower():
        await message.channel.send(f'¡Hello {message.author.name}!')

    await bot.process_commands(message)

# Execution
bot.run(token)        


