from   Constants import PROFANITY, CARRIAGE_RETURN, BUFFER
from   Config    import HOST, PORT, PASS, NICK, CHANNEL
from socket import *

class Bot(object):
    def __init__(self):
        self.socket = socket()

        self.openSocket()
        self.joinRoom()
        self.listen()

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
                ### DEBUG ###
                print (line)
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
        while True:
            readbuffer = readbuffer + self.socket.recv(BUFFER).decode("UTF-8")
            temp = readbuffer.split("\n")
            readbuffer = temp.pop()
            
            for line in temp:
                    print(line)
                    if "PING" in line:
                            s.send(line.replace("PING", "PONG"))
                            break
                    user = self.getUser(line)
                    message = self.getMessage(line)
                    print (user + ": " + message)
                    self.decideResponse(user, message)

    def decideResponse(self, user, message):
        message = message.lower()
        print (message)
        output = ""
        if (user == "generaldave" and message == "!quote"):
            output = "Hello World"
        elif (message == "you suck"):
            output = "".join((user, ", you suck even more."))        
        elif ("you suck" in message):
            output = "".join((user + ", there will be no sucking around here."))
        elif ("hello" in message):
            output = "".join((user + ", hello and welcome to my stream."))
        elif ([word for word in message.split(" ") if word in PROFANITY]):
            output = "".join((user + ", such language. My virtual ears hurt."))
        if (output):
            self.sendMessage(output)
        
    def sendMessage(self, message):
        tempMessage = "PRIVMSG #" + CHANNEL + " :" + message
        self.socket.send((tempMessage + CARRIAGE_RETURN).encode("UTF-8"))

        ### DEBUG ###
        print ("Sent: " + tempMessage)
