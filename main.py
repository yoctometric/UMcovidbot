import discord
from discord.ext import commands
import asyncio
import pagescraper

# define bot
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("Launched UMcovidbot")
    # initiate main loop
    bot.loop.create_task(main_loop())


@bot.command()
async def update(ctx):
    # ignore if not from whitelisted channel
    if not ctx.channel.id in whitelisted_channels:
        return

    # when user calls update, send an update
    date, count, link = await pagescraper.get_latest_um_update()
    # set up the embed
    print(link)
    embed = discord.Embed(title="UMaine Orono Campus Case Update: ", url=link, description=f"{count} as of {date}", color= discord.Colour.dark_blue())
    await ctx.send(embed=embed)


# main loop
async def main_loop():
    while True:
        await asyncio.sleep(30)


def load_parameters():
    # loads data from the config file.
    chans = []
    token = ''

    with open('config.txt', 'r') as f:
        # naively parse the data
        for line in f.readlines():
            if line.startswith('channels:'):
                line = line[9:].replace("\n", "")
                cs = line.split(',')
                for c in cs:
                    chans.append(int(c))

            elif line.startswith('token:'):
                token = line[6:].replace("\n", "")

        return token, chans


# load in config settings
bot_token, whitelisted_channels = load_parameters()

# start the bot
bot.run(bot_token)
