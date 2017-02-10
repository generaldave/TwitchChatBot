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
import datetime              # For timer
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

    # Mehtod starts timer
    def startTimer(self) -> None:
        self.start = datetime.datetime.now()
        self.timer = str(datetime.datetime.now() - self.start)

    # Method returns timer
    def getTimer(self, full: bool) -> str:
        if self.timer and self.start:
            if full:
                self.timer = str(datetime.datetime.now() - self.start)
            else:
                self.timer = datetime.datetime.now() - self.start
                hours, remainder = divmod(self.timer.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.timer = "%02d" % minutes + ":" + "%02d" % seconds
        return self.timer

    # Method stops timer
    def stopTimer(self) -> None:
        self.start = None

    # Method displays split
    def display(self) -> None:
        ten = 1

    # Method handles toString
    def __str__(self):
        return "Attempts: " + self.attempts + "\n" + \
               "Image: "    + self.image    + "\n" + \
               "Label: "    + self.label    + "\n" + \
               "Average: "  + self.average
