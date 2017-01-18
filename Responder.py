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

from   Constants   import     *   # Constants file
from   FileHandler import     *   # File handler class
from   StringTokenizer import *   # String tokenizer class
import random                     # Random numbers class

########################################################################
#                                                                      #
#                           RESPONDER CLASS                            #
#                                                                      #
########################################################################

class Responder(object):
    def __init__(self, directory: str) -> None:
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

    # Method find random number if possible, otherwise state so
    def findRandom(self, user: str, message: str) -> str:
        message = message.split(" ")
        num1 = message[1]
        num2 = message[2]
        if (self.tryInt(num1) and self.tryInt(num2)):
            rnd  = str(random.randint(int(num1), int(num2)))
            response = user + ", I chose "  + rnd  + \
                       " randomly between " + num1 + " and " + num2
        else:
            response = user + ", I can't find numbers between strings."

        return response

    # Method decides which quote to display
    def findQuote(self, user: str, message: str) -> str:
        index = random.randint(0, len(self.quotes) - 1)
        return self.quotes[index]
    
    # Method adds quote
    def addQuote(self, user: str, message: str) -> str:
        try:
            index    = message.index(" ")
            self.quotes.append(message[index + 1:])
            response = user + ", \"" + message[index + 1:] + \
                       "\" added to quotes."
        except:
            response = user + ", that is not a valid quote."

        return response

    # Method decides if bot should respond and how to respond
    def decideResponse(self, user: str, message: str) -> str:
        message = message.lower()
        response = ""

        # Handles !random command
        if message.startswith("!random"):
            response = self.findRandom(user, message)

        # Handles !quote command
        elif message == "!quote":
            response = self.findQuote(user, message)

        # Handles !addquote command
        elif message.startswith("!addquote"):
            response = self.addQuote(user, message)

        # Handles Hello message
        elif message.startswith("hello"):
            response = user + ", hello and welcome to my stream."

        # Handles profanity response
        elif ([word for word in message.split(" ") if word in PROFANITY]):
            response = user + ", such language. My virtual ears hurt."

        return response

    # Method populates quotes array
    def populateQuotes(self) -> None:
        fileObj = FileHandler(self.directory, "Quotes")
        quotesArray = fileObj.read()
        tokenizer = StringTokenizer("\n")
        tokenizer.setString(quotesArray)

        while not tokenizer.atEnd():
            token = tokenizer.getToken()
            self.quotes.append(token)
