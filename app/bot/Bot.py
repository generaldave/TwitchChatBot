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

from   .Constants import *        # Constants file
from   .Config    import *        # Config file
from   socket     import *        # Sockets class
from   .Responder import *        # Responder class
from   threading  import Thread   # For threading

########################################################################
#                                                                      #
#                              BOT CLASS                               #
#                                                                      #
########################################################################

class Bot(Thread):
    appHint = "init.py"
    
    def __init__(self, app: appHint, directory: str) -> None:
        Thread.__init__(self)
        self.socket    = socket()
        self.directory = directory
        self.app       = app

        self.responder = Responder(self.app, self.directory)
        self.listening = True
        
        self.openSocket()
        self.joinRoom()

    # Method stops bot
    def stop(self) -> None:
        self.listening = False

    # Method opens bot's socket
    def openSocket(self) -> None:
        self.socket.connect((HOST, PORT))
        self.socket.send(("PASS "  + PASS    + CARRIAGE_RETURN).encode("UTF-8"))
        self.socket.send(("NICK "  + NICK    + CARRIAGE_RETURN).encode("UTF-8"))
        self.socket.send(("JOIN #" + CHANNEL + CARRIAGE_RETURN).encode("UTF-8"))

    # Method joins Twitch chat room
    def joinRoom(self) -> None:
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
        message = "reporing for duty."
        self.app.chatBlock.displayMessage(NICK, message)

    # Method returns user name of a given input message
    def getUser(self, line: str) -> None:
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user

    # Method returns the actual message of a given input message
    def getMessage(self, line: str) -> None:
        separate = line.split(":", 2)
        message = separate[2]
        return message.rstrip(CARRIAGE_RETURN)

    # Method listens for incoming messages from Twitch
    def run(self) -> None:
        while self.listening:
            readbuffer = ""
            readbuffer = readbuffer + self.socket.recv(BUFFER).decode("UTF-8")
            temp = readbuffer.split("\n")
            readbuffer = temp.pop()
            
            for line in temp:                
                if "PING" in line:
                    self.socket.send(line.replace("PING", "PONG").encode("UTF-8"))
                    break
                user    = self.getUser(line)
                message = self.getMessage(line)
                self.app.chatBlock.displayMessage(user, message)
                self.decideResponse(user, message)

    # Method decides if bot should respond and how to respond
    def decideResponse(self, user: str, message: str) -> None:
        response = self.responder.decideResponse(user, message)
        
        # Only send a response if there is one
        if (response):
            self.sendMessage(response)
            self.app.chatBlock.displayMessage("mastergunsbot", response)

    # Method sends message back to Twitch
    def sendMessage(self, message):
        tempMessage = "PRIVMSG #" + CHANNEL + " :" + message + CARRIAGE_RETURN
        self.socket.send((tempMessage).encode("UTF-8"))
