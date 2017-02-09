########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Splits Class: Block for splits                                       #
#                                                                      #
# Created on 2017-2-5                                                  #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   .Constants   import *   # Constants file
from   .filehandler import *   # File handler package
from   .Split       import *   # Split class
import datetime                # For timer
import pygame                  # For GUI

########################################################################
#                                                                      #
#                            SPLITS CLASS                              #
#                                                                      #
########################################################################

class Splits(object):
    screenHint = "Pygame screen"   # Type hinting
    
    def __init__(self, screen: screenHint, directory: str) -> None:
        self.screen    = screen
        self.directory = directory

        # Data members
        self.splits = []    

        # Attributes
        self.goodSplit = COLOUR['GREEN']
        self.badSplit  = COLOUR['RED']
        self.rectangle = (10, 220, 200, 420)

        ##### DEBUG #####
        self.start = datetime.datetime.now()

        # Set up
        self.setTheme(STANDARD)
        self.chooseGame()
        self.setupGUI()

    # Method sets theme
    def setTheme(self, theme: int) -> None:
        self.rectangleColor = BLOCK[theme]
        self.normalFont     = TEXT_COLOUR[theme]
        self.adminFont      = ADMIN_COLOUR[theme]

    # Method sets up GUI
    def setupGUI(self) -> None:
        self.font = pygame.font.SysFont("monospace", 15)
        
        self.splitsRect = pygame.draw.rect(self.screen, self.rectangleColor,
                                           self.rectangle)

        # Display splits
        imgX     = 20        
        labelX   = 50
        averageX = 155
        imgY     = 240
        textY    = 244

        # Attempts
        attemptsText = self.font.render("Attempts: " + \
                                        self.splits[0].getAttempts(), \
                                        0, self.adminFont)
        self.screen.blit(attemptsText, (83, 222))

        # Splits
        for split in self.splits:
            img         = pygame.image.load(split.getImage())
            labelText   = self.font.render(split.getLabel(),   \
                                           0, self.normalFont)
            timerText   = self.font.render(split.getAverage(), \
                                           0, self.adminFont)
            averageText = self.font.render(split.getAverage(), \
                                           0, self.normalFont)

            self.screen.blit(img, (imgX, imgY))
            self.screen.blit(labelText, (labelX, textY))
            self.screen.blit(timerText, (95, textY))
            self.screen.blit(averageText, (averageX, textY))

            imgY  = imgY  + 30
            textY = textY + 30

        # Overall
        now = str(datetime.datetime.now() - self.start)
        overallText = self.font.render(now, 0, self.adminFont)
        self.screen.blit(overallText, (48, 605))

    # Method chooses game
    def chooseGame(self) -> None:
        game = LOST_LEVELS
        self.populateSplits(LOST_LEVELS)

    # Method sets up splits
    def populateSplits(self, game: int) -> None:
        path = self.directory + "/files/splits/"
        if game == LOST_LEVELS:
            file = "lostlevels"
        fileObj = FileHandler(path, file)
        splitsArray = fileObj.read()
        tokenizer = StringTokenizer("\n")
        tokenizer.setString(splitsArray)

        # Number of attemtps
        token    = tokenizer.getToken()
        attempts = token

        # Splits information
        while not tokenizer.atEnd():
            token = tokenizer.getToken()
            
            # Image
            index = token.index(",")
            image = token[:index]
            token = token[index + 1:]
            
            # Label
            index = token.index(",")
            label = token[:index]

            # Average
            average = token[index + 1:]

            # Append split
            split = Split(self.screen, self.directory)
            split.setupSplit(attempts, image, label, average, game)
            self.splits.append(split)

    # Method updates splits block
    def update(self) -> None:
        self.setupGUI()
