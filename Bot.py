########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Bot class: Handles sockets part of bot                               #
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
from   Config    import *   # Config file
from   socket    import *   # Sockets class

########################################################################
#                                                                      #
#                              BOT CLASS                               #
#                                                                      #
########################################################################

class Bot(object):
    appHint = "init.py"
    def __init__(self, app: appHint) -> None:
        self.socket = socket()
        self.app    = app

        self.openSocket()
        self.joinRoom()

    # Method opens bot's socket
    def openSocket(self) -> None:
        self.socket.connect((HOST, PORT))
        self.socket.send(("PASS "  + PASS    + CARRIAGE_RETURN).encode("UTF-8"))
        self.socket.send(("NICK "  + NICK    + CARRIAGE_RETURN).encode("UTF-8"))
        self.socket.send(("JOIN #" + CHANNEL + CARRIAGE_RETURN).encode("UTF-8"))

    # Method joins Twitch chat room
    def joinRoom(self):
        readbuffer = ""
        
        loading = True
        while loading:
            readbuffer = readbuffer + self.socket.recv(BUFFER).decode("UTF-8")
            temp = readbuffer.split("\n")
            readbuffer = temp.pop()

            for line in temp:
                if ("End of /NAMES list" in line):
                    loading = False
                    
        self.sendMessage("reporting for duty.")

    # Method returns user name of a given input message
    def getUser(self, line):
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user

    # Method returns the actual message of a given input message
    def getMessage(self, line):
        separate = line.split(":", 2)
        message = separate[2]
        return message.rstrip(CARRIAGE_RETURN)

    # Method listens for incoming messages from Twitch
    def listen(self):
        readbuffer = ""
        readbuffer = readbuffer + self.socket.recv(BUFFER).decode("UTF-8")
        temp = readbuffer.split("\n")
        readbuffer = temp.pop()
        
        for line in temp:
            if "PING" in line:
                self.socket.send(line.replace("PING", "PONG"))
                break
            user    = self.getUser(line)
            message = self.getMessage(line)
            self.app.chatBlock.displayMessage(user, message)
            self.decideResponse(user, message)

    # Method decides if bot should respond and how to respond
    def decideResponse(self, user, message):
        message = message.lower()
        output = ""
        if (user == "generaldave" and message == "!quote"):
            output = "Hello World"
        elif (message == "you suck"):
            output = user + ", you suck even more."
        elif ("you suck" in message):
            output = user + ", there will be no sucking around here."
        elif ("hello" in message):
            output = user + ", hello and welcome to my stream."
        elif ([word for word in message.split(" ") if word in PROFANITY]):
            output = user + ", such language. My virtual ears hurt."
        if (output):
            self.sendMessage(output)
            self.app.chatBlock.displayMessage("mastergunsbot", output)

    # Method sends message back to Twitch
    def sendMessage(self, message):
        tempMessage = "PRIVMSG #" + CHANNEL + " :" + message
        self.socket.send((tempMessage + CARRIAGE_RETURN).encode("UTF-8"))
