########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Title Class: Block for game title - for YouTube only                 #
#                                                                      #
# Created on 2017-2-10                                                 #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   .Constants   import *   # Constants file
from   .filehandler import *   # File handler package
import pygame                  # For GUI

########################################################################
#                                                                      #
#                            TITLE CLASS                               #
#                                                                      #
########################################################################

class Title(object):
    screenHint = "Pygame screen"
    
    def __init__(self, screen: screenHint, appDirectory: str) -> None:
        self.screen    = screen
        self.directory = appDirectory

        # Lines of game title
        self.lines = []
        self.populateLines()

        # Rectangle attributes
        self.width     = 330
        self.height    = SCREEN_HEIGHT - 20
        self.x         = SCREEN_WIDTH  - self.width - 10
        self.y         = 10
        self.rectangle = (self.x, self.y, \
                          self.width, self.height)

        # Set up GUI
        self.setTheme(STANDARD)
        self.setupGUI()

    # Method sets theme
    def setTheme(self, theme: int) -> None:
        self.rectangleColor = BLOCK[theme]
        self.normalFont     = TEXT_COLOUR[theme]
        self.adminFont      = ADMIN_COLOUR[theme]

    # Mehthod sets up GUI
    def setupGUI(self) -> None:
        self.fontSize = 72
        
        self.titleRect = pygame.draw.rect(self.screen,         \
                                          self.rectangleColor, \
                                          self.rectangle)

    # Method updates game server block
    def update(self) -> None:
        self.setupGUI()

        y = 100
        fontSize = self.fontSize
        colour    = self.adminFont
        for i in range(len(self.lines)):
            line = self.lines[i]
            end  = len(self.lines) - 1
            if i == end:
                fontSize = 40
                colour = self.normalFont
            self.font = pygame.font.SysFont("arial black", fontSize)
            width, height = self.font.size(line)
            while width >= self.width - 20:
                fontSize = fontSize - 1
                self.font = pygame.font.SysFont("arial black", fontSize)
                width, height = self.font.size(line)
            
            x = self.x - (width / 2) + (self.width / 2)
            text = self.font.render(line, 0, colour)
            self.screen.blit(text, (x, y))
            y = y + (self.fontSize * 2)

    # Method populates lines array
    def populateLines(self) -> None:
        # Set up file object
        path = self.directory + "/files/"
        file = "title"
        fileObj = FileHandler(path, file)
        linesArray = fileObj.read()

        # Set up tokenizer
        tokenizer = StringTokenizer("\n")
        tokenizer.setString(linesArray)

        # Populate lines array
        while not tokenizer.atEnd():
            token = tokenizer.getToken()
            self.lines.append(token)
