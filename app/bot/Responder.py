########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Responder class: Handles bot responses                               #
#                                                                      #
# Created on 2016-1-18                                                 #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   .Constants   import *   # Constants file
from   .filehandler import *   # File handler package
import random                  # Random numbers class
import re                      # Used for regex

########################################################################
#                                                                      #
#                           RESPONDER CLASS                            #
#                                                                      #
########################################################################

class Responder(object):
    appHint = "init.py"
    
    def __init__(self, app: appHint, directory: str) -> None:
        self.app       = app
        self.directory = directory
        self.quotes    = []
        
        self.populateQuotes()

    # Method decides whether a string can be an integer
    def tryInt(self, string: str) -> bool:
        try:
            int(string)
            return True
        except ValueError:
            return False

    # Method decides theme value
    def decideValue(self, value: str) -> int:
        if value == "pathofexile":
            return 1
        elif value == "coding":
            return 2
        elif value == "retrogaming":
            return 3
        else:
            return 0

    # Method changes theme
    def changeTheme(self, user: str, message: str) -> str:
        message = message.split(" ")
        theme = message[1]
        theme = self.decideValue(theme)
        if (self.tryInt(theme)):
            self.app.setTheme(theme)
            response = user + ", theme successfully changed."
        else:
            response = user + ", invalid theme."
        return response

    # Method changes YouTube
    def changeYoutube(self, user: str, message: str) -> str:
        try:
            message = message.split(" ")
            youtube = message[1]
            if youtube == "on":
                self.app.setYoutube(True)
            elif youtube == "off":
                self.app.setYoutube(False)
            else:
                return user + ", " + "invalid command."
        except:
            return user + ", " + "try the format: !youtube <on, off>."

    # Method decides 8 ball response
    def eightBall(self, user: str, message: str) -> str:
        try:
            message = message.split(" ")
            if message[0] == "!8ball" and message[1]:
                index = random.randint(0, len(EIGHT_BALL))
                return user + ", " + EIGHT_BALL[index]
            else:
                return user + ", was that even a question?"
        except:
            return user + ", try the format: !8ball question."

    # Method find random number if possible, otherwise state so
    def findRandom(self, user: str, message: str) -> str:
        try:
            message = message.split(" ")
            num1 = message[1]
            num2 = message[2]
            if (self.tryInt(num1) and self.tryInt(num2)):
                rnd  = str(random.randint(int(num1), int(num2)))
                response = user + ", I chose "  + rnd  + \
                           " randomly between " + num1 + " and " + num2
            else:
                response = user + ", I can't find numbers between strings."
        except:
            response = user + ", invalid input. Try this format: " + \
                       "!random lower upper"
        return response

    # Method decides which quote to display
    def findQuote(self, user: str, message: str) -> str:
        try:
            index = random.randint(0, len(self.quotes) - 1)
            return self.quotes[index]
        except:
            return user + ", acceptable format: !addquote quote"
    
    # Method adds quote
    def addQuote(self, user: str, message: str) -> str:
        try:
            index    = message.index(" ")
            text     = message[index + 1:]
            self.quotes.append(text)
            response = user + ", \"" + text + "\" added to quotes."
            fileObj  = FileHandler(self.directory + "/files/", "Quotes")
            fileObj.write(self.quotes, "\n")
        except:
            response = user + ", that is not a valid quote."

        return response

    # Method decides if bot should respond and how to respond
    def decideResponse(self, user: str, message: str) -> str:
        message = message.lower()
        response = ""

        chars = [".", ",", "!"]

        # Handles Admin commands
        if user == "generaldave":
            # !theme
            if message.startswith("!theme"):           
                response = self.changeTheme(user, message)

            # !youtube
            elif message.startswith("!youtube"):
                response = self.changeYoutube(user, message)

        # Handles !8ball command
        elif message.startswith("!8ball"):
            response = self.eightBall(user, message)

        # Handles !random command
        elif message.startswith("!random"):
            response = self.findRandom(user, message)

        # Handles !quote command
        elif message == "!quote":
            response = self.findQuote(user, message)

        # Handles !addquote command
        elif message.startswith("!addquote"):
            response = self.addQuote(user, message)

        # Handles greeting messages
        elif ([word for word in message.split(" ") \
              if re.sub('\W+', '', word) in GREETINGS]):
            response = user + ", hello and welcome to my stream."

        # Handles profanity response        
        elif ([word for word in message.split(" ") \
               if re.sub('\W+', '', word) in PROFANITY]):
            response = user + ", such language. My virtual ears hurt."

        return response

    # Method populates quotes array
    def populateQuotes(self) -> None:
        fileObj = FileHandler(self.directory + "/files/", "Quotes")
        quotesArray = fileObj.read()
        tokenizer = StringTokenizer("\n")
        tokenizer.setString(quotesArray)

        while not tokenizer.atEnd():
            token = tokenizer.getToken()
            self.quotes.append(token)
