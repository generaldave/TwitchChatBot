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

from   Constants import *   # Constants file
import random               # Random numbers class

########################################################################
#                                                                      #
#                           RESPONDER CLASS                            #
#                                                                      #
########################################################################

class Responder(object):
    def __init__(self) -> None:
        ten = 1

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
        return "git commit -m \"updated file\" ~ Dave (2017, January 18)"

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

        # Handles Hello message
        elif message.startswith("hello"):
            response = user + ", hello and welcome to my stream."

        # Handles profanity response
        elif ([word for word in message.split(" ") if word in PROFANITY]):
            response = user + ", such language. My virtual ears hurt."

        return response
        
