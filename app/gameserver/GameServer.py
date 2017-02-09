########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Game Server Class: Block for playing mini games and doing raffles    #
#                                                                      #
# Created on 2017-2-5                                                  #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   .Constants import *   # Constants file
import pygame                # For GUI

########################################################################
#                                                                      #
#                          GAMESERVER CLASS                            #
#                                                                      #
########################################################################

class GameServer(object):
    screenHint = "Pygame screen"
    
    def __init__(self, screen: screenHint, appDirectory: str) -> None:
        self.screen    = screen
        self.directory = appDirectory

        # Rectangle attributes
        self.width     = 330
        self.height    = (SCREEN_HEIGHT / 2) - 15
        self.x         = SCREEN_WIDTH- self.width - 10
        self.y         = 20
        self.rectangle = (self.x, self.height + 20, \
                          self.width, self.height)

        # Set up GUI
        self.setTheme(STANDARD)
        self.setupGUI()

    # Method sets theme
    def setTheme(self, theme: int) -> None:
        self.rectangleColor = BLOCK[theme]

    # Mehthod sets up GUI
    def setupGUI(self) -> None:
        self.gameserverImage = pygame.image.load(self.directory + \
                               "/images/gameserverdown.png")

    # Method updates game server block
    def update(self) -> None:
        self.gameserverRect = pygame.draw.rect(self.screen,         \
                                               self.rectangleColor, \
                                               self.rectangle)
        self.screen.blit(self.gameserverImage, self.gameserverRect)
