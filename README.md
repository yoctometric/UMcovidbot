# UMcovidbot

A bot written by William Cunningham. Not particularly user friendly, because I don't expect anybody to use it.

Note: this bot depends on the discord.py, requests, and asyncio libraries. Make sure you have them installed!

REQUIRES A CONFIG FILE!
to use, create a text file named 'config.txt' in the same directory as main.py. 
The format of the file should be as follows:

token:&lt;discord bot token&gt;
channels:&lt;channel id number&gt;,&lt;channel id number&gt;,&lt;channel id number&gt;,&lt;channel id number&gt;

any lines not starting with 'token:' or 'channels:' will be ignored

to get an update, simply type '!update' in a whitelisted channel in a server your instance of the bot is running in.
