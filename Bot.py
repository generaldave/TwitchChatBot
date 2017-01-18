from   Constants import PROFANITY, CARRIAGE_RETURN, BUFFER
from   Config    import HOST, PORT, PASS, NICK, CHANNEL
from socket import *

class Bot(object):
    def __init__(self, app):
        self.socket = socket()
        self.app    = app

        self.openSocket()
        self.joinRoom()

    def openSocket(self):
        self.socket.connect((HOST, PORT))
        self.socket.send(("PASS "  + PASS    + CARRIAGE_RETURN).encode("UTF-8"))
        self.socket.send(("NICK "  + NICK    + CARRIAGE_RETURN).encode("UTF-8"))
        self.socket.send(("JOIN #" + CHANNEL + CARRIAGE_RETURN).encode("UTF-8"))

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

    def getUser(self, line):
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user

    def getMessage(self, line):
        separate = line.split(":", 2)
        message = separate[2]
        return message.rstrip(CARRIAGE_RETURN)

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
        
    def sendMessage(self, message):
        tempMessage = "PRIVMSG #" + CHANNEL + " :" + message
        self.socket.send((tempMessage + CARRIAGE_RETURN).encode("UTF-8"))

        print ("Sent:" + tempMessage)
