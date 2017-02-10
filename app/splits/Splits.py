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
        self.game    = None
        self.overall = None
        self.splits  = []
        self.timing  = False
        self.index   = 0

        # Attributes
        self.goodSplit = COLOUR['GREEN']
        self.badSplit  = COLOUR['RED']
        self.rectangle = (10, 220, 200, 420)        

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
                                        self.attempts, \
                                        0, self.adminFont)
        self.screen.blit(attemptsText, (83, 222))

        # Splits
        for split in self.splits:
            img         = pygame.image.load(split.getImage())
            labelText   = self.font.render(split.getLabel(),   \
                                           0, self.normalFont)            
            averageText = self.font.render(split.getBest(), \
                                           0, self.normalFont)

            self.screen.blit(img, (imgX, imgY))
            self.screen.blit(labelText, (labelX, textY))            
            self.screen.blit(averageText, (averageX, textY))

            imgY  = imgY  + 30
            textY = textY + 30

        if not self.overall:
            self.overall = Split(self.screen, self.directory)

    # Method handles button press - if Select start/stop split timers
    def buttonPressed(self, button: int):
        if button == SELECT:
            if self.index < len(self.splits) - 1:
                if not self.timing:
                    self.timing = True
                    self.overall.startTimer()
                else:
                    timer = self.splits[self.index].getTimer(False)
                    best  = self.splits[self.index].getBest()
                    if (timer < best or best == "00:00"):
                        self.splits[self.index].setBest(timer)
                    self.splits[self.index].stopTimer()
                    self.index = self.index + 1
                self.splits[self.index].startTimer()
            else:
                self.overall.stopTimer()
                self.splits[self.index].stopTimer()

    # Method handles resetting of timer
    def resetTimer(self) -> None:
        self.attempts = "%03d" % (int(self.attempts) + 1)
        self.storeSplits()
        self.overall = None
        self.splits  = []
        self.timing  = False
        self.index   = 0
        self.chooseGame()
        self.setupGUI()

    # Method chooses game
    def chooseGame(self) -> None:
        self.game = LOST_LEVELS
        self.populateSplits()

    # Method sets up splits
    def populateSplits(self) -> None:
        path = self.directory + "/files/splits/"
        if self.game == LOST_LEVELS:
            file = "lostlevels"
        fileObj = FileHandler(path, file)
        splitsArray = fileObj.read()
        tokenizer = StringTokenizer("\n")
        tokenizer.setString(splitsArray)

        # Number of attemtps
        token         = tokenizer.getToken()
        self.attempts = token

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
            split.setupSplit(image, label, average, self.game)
            self.splits.append(split)

    # Method rewrites splits to file
    def storeSplits(self) -> None:
        tempSplits = []        
        path       = self.directory + "/files/splits/"
        
        if self.game == LOST_LEVELS:
            file = "lostlevels"
            
        fileObj = FileHandler(path, file)
        
        tempSplits.append(self.attempts)  
        for split in self.splits:
            img = split.getImage()
            index = img.rindex("/")
            img = img[index + 1:]
            tempSplits.append(img              + "," + \
                              split.getLabel() + "," + \
                              split.getBest())
        
        fileObj.append(tempSplits, "\n")

    # Method updates splits block
    def update(self) -> None:
        self.setupGUI()
        # Timer
        timerX   = 95
        timerY   = 244
        for split in self.splits:
            if split.getTimer(False):                
                timerText = self.font.render(split.getTimer(False), \
                                             0, self.adminFont)
                self.screen.blit(timerText, (timerX, timerY))
                timerY = timerY + 30

        # Overall
        overallText = self.font.render(self.overall.getTimer(True), \
                                       0, self.adminFont)
        self.screen.blit(overallText, (48, 605))
        

    
