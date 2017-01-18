##from Button import *   # Button Class
from Config import NICK
from Constants import *
import pygame   # For GUI

class ChatBlock(object):
    def __init__(self, screen):
        self.screen = screen   # Main screen

        self.rectangle = (10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        self.rectangleColor = WHITE

        self.font      = pygame.font.SysFont("Helvetica", 14)
        self.fontColor = BLACK

        self.y = 20

        self.setupRectangle()

    def setupRectangle(self):
        self.chatRectangle = pygame.draw.rect(self.screen,         \
                                              self.rectangleColor, \
                                              self.rectangle)

    def displayMessage(self, user, message):
        if user == NICK:
            self.fontColor = RED
        self.chat = self.font.render(user + " : " + message, \
                         True, \
                         self.fontColor)
        self.screen.blit(self.chat, (20, self.y))

        self.y = self.y + 20

        self.fontColor = BLACK
