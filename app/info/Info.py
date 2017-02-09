########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Info Class: Block for random info                                    #
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
#                             INFO CLASS                               #
#                                                                      #
########################################################################

class Info(object):
    screenHint = "Pygame screen"
    
    def __init__(self, screen: screenHint, directory: str) -> None:
        self.screen    = screen
        self.directory = directory

        self.rectangle = (10, 790, 1558, 204)

        self.setTheme(STANDARD)
        self.update()   # sets up GUI

    # Method sets theme
    def setTheme(self, theme: int) -> None:
        self.rectangleColor = BLOCK[theme]

        if theme == RETROGAMING:
            self.banner = pygame.image.load(self.directory + \
                                            "/images/retrobanner.png")
        elif theme == CODING:
            self.banner =  pygame.image.load(self.directory + \
                                            "/images/codingbanner.png")
        elif theme == PATHOFEXILE:
            self.banner =  pygame.image.load(self.directory + \
                                            "/images/poebanner.png")
        else:
            self.banner = None

    # Method updates web cam block
    def update(self) -> None:
        self.infoRect = pygame.draw.rect(self.screen, self.rectangleColor,
                                         self.rectangle)
        if self.banner:
            self.screen.blit(self.banner, (10, 790))
