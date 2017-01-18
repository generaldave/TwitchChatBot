##from Button import *   # Button Class
from Config import NICK
from Constants import *
import pygame   # For GUI

# Chat block holds 22 lines. Each line after needs to move up 20px
# And 46 characters wide

class ChatBlock(object):
    def __init__(self, screen):
        self.screen = screen   # Main screen

        self.rectangle = (10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        self.rectangleColor = WHITE

        self.font      = pygame.font.SysFont("Helvetica", 14)
        self.fontColor = BLACK

        self.y = 20

        self.messages = []

        self.lineCount = 0

        self.setupRectangle()

    def getLineCount(self):
        return self.lineCount

    def setupRectangle(self):
        self.chatRectangle = pygame.draw.rect(self.screen,         \
                                              self.rectangleColor, \
                                              self.rectangle)

    def displayMessage(self, user, message):
        if user == NICK:
            self.fontColor = RED

        lines = []
        text = user + " : " + message
        length = len(text)
        if length <= 46:
            
            self.messages.append(text)
            self.chat = self.font.render(text, \
                             True, \
                             self.fontColor)
            self.screen.blit(self.chat, (20, self.y))
            self.lineCount = self.lineCount + 1

            self.y = self.y + 20

        else:
            lines.append(text[:46])
            message = text[46:]
            length = len(message)
            text = lines[0]
            self.messages.append(text)
            self.chat = self.font.render(text, \
                             True, \
                             self.fontColor)
            self.screen.blit(self.chat, (20, self.y))
            self.lineCount = self.lineCount + 1

            self.y = self.y + 20
            
            while length > 46:
                lines.append(message[:46])
                message = message[46:]
                length = len(message)
            lines.append(message)
        if lines:
            for i in range(1, len(lines)):
                text = lines[i]
                self.messages.append(text)
                self.chat = self.font.render(text, \
                                 True, \
                                 self.fontColor)
                self.screen.blit(self.chat, (20, self.y))
                self.lineCount = self.lineCount + 1

                self.y = self.y + 20

        self.fontColor = BLACK
