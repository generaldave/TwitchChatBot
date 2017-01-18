########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# ChatBlock class: Chat window to capture Twitch chat                  #
#                                                                      #
# Created on 2016-1-18                                                 #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Config    import *   # Config file
from   Constants import *   # Constants file
import pygame               # For GUI

########################################################################
#                                                                      #
#                            CHATBLCOK CLASS                           #
#                                                                      #
########################################################################

# Chat block holds 22 lines. Each line after needs to move up 20px
# And 46 characters wide

class ChatBlock(object):
    screenHint = "A PyGame screen"
    
    def __init__(self, screen: screenHint) -> None:
        self.screen = screen   # Main screen

        # Rectangle attributes
        self.rectangle = (10, 10, SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
        self.rectangleColor = BLOCK[THEME]

        # Chat attributes
        self.font      = pygame.font.SysFont("Helvetica", 14)
        self.fontColor = TEXT_COLOUR[THEME]
        self.y = 20
        self.lineCount = 0
        self.messages = []
        self.index = 0

        # Set up rectangle
        self.setupRectangle()

    # Method returns line count
    def getLineCount(self) -> int:
        return self.lineCount

    # Method displays rectangle
    def setupRectangle(self) -> None:
        self.chatRectangle = pygame.draw.rect(self.screen,         \
                                              self.rectangleColor, \
                                              self.rectangle)

    # Method displays chat messages
    def displayMessage(self, user: str, message: str) -> None:
        # If user is the bot, set colour to red to stand out
        if user == NICK:
            self.fontColor = ADMIN_COLOUR[THEME]

        text = user + " : " + message
        length = len(text)
        while length > 46:
            self.messages.append((text[:46], self.fontColor))
            text = text[46:]
            length = len(text)
        self.messages.append((text, self.fontColor))


    # Method updates chat block
    def update(self) -> None:
        self.setupRectangle()
        y = self.y
        self.lineCount = 0
        for i in range(self.index, len(self.messages)):
            text  = self.messages[i][0]
            color = self.messages[i][1]
            self.chat = self.font.render(text, True, color)
            self.screen.blit(self.chat, (20, y))
            self.lineCount = self.lineCount + 1

            y = y + 20

        if self.lineCount > 22:
            self.index = self.index + 1
            self.screen.fill(BACKGROUND[THEME])
            self.update()
        self.fontColor = TEXT_COLOUR[THEME]
