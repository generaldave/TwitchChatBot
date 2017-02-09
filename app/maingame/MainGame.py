########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Main Game: Block for the main game                                   #
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
#                            MAINGAME CLASS                            #
#                                                                      #
########################################################################

class MainGame(object):
    screenHint = "Pygame screen"
    
    def __init__(self, screen: screenHint) -> None:
        self.screen = screen

        self.rectangle = (220, 10, 1348, 770)

        self.setTheme(STANDARD)
        self.update()   # sets up GUI

    # Method sets theme
    def setTheme(self, theme: int) -> None:
        self.rectangleColor = BLOCK[theme]

    # Method updates main game block
    def update(self) -> None:
        self.gameRect = pygame.draw.rect(self.screen, self.rectangleColor,
                                         self.rectangle)
