Twitch Chat Bot

- Written in Python 3.4.3
- Using PyGame 1.9.2b1

This is a Twitch Chat Bot in progress.

So far it will connect to my chat, respond to a couple phrases, and react to a few commands.

It also keeps track of messages in its own window.

![screenshot](https://cloud.githubusercontent.com/assets/7481680/22080952/91aa7530-dd8f-11e6-928c-06934891857e.png)

The bot's chat window is very basic and I am working on theming it so it will look nicer. I also need to work on word wrapping instead of letter wrapping.

In order for it to work you need to create a new file in the directory called Config.py and add these lines to it:

from Constants import *

HOST    = "irc.twitch.tv"
PORT    = 6667
PASS    = "oauth: gotten from https://twitchapps.com/tmi"
NICK    = "Twitch account name of bot"
CHANNEL = "Channel name for bot to join"
