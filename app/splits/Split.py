########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Split Class: Split object                                            #
#                                                                      #
# Created on 2017-2-8                                                  #
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
#                            SPLIT CLASS                               #
#                                                                      #
########################################################################

class Split(object):
    screenHint = "Pygame screen"   # Type hinting
        
    def __init__(self, screen: screenHint, directory: str) -> None:
        self.screen        = screen
        self.imgDirectory  = directory + "/images/splits/"
        self.fileDirectory = directory + "/files/splits/"

        # Data memebers
        self.attempts = None
        self.image    = None
        self.label    = None
        self.average  = None
        self.game     = None
        self.timer    = None
        self.start    = None

    # Method returns attempts
    def getAttempts(self) -> str:
        return self.attempts

    # Method returns image
    def getImage(self) -> str:
        return self.image

    # Method returns label
    def getLabel(self) -> str:
        return self.label

    # Method returns average
    def getAverage(self) -> str:
        return self.average

    # Method sets up a split
    def setupSplit(self, attempts: str, image: str, label: str, \
                   average: str, game: int) -> None :
        if game == LOST_LEVELS:
            folder = "lostlevels/"
        self.attempts = attempts
        self.image    = self.imgDirectory + folder + image
        self.label    = label
        self.average  = average
        self.game     = game

    # Mehtod handles timer - start, stop, new
    def handleTimer(self) -> None:
        ten = 1

    # Method displays split
    def display(self) -> None:
        ten = 1

    # Method handles toString
    def __str__(self):
        return "Attempts: " + self.attempts + "\n" + \
               "Image: "    + self.image    + "\n" + \
               "Label: "    + self.label    + "\n" + \
               "Average: "  + self.average
