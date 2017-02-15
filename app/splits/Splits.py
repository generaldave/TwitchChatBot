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
        self.game        = None
        self.overall     = None
        self.splits      = []
        self.timing      = False
        self.index       = 0

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
        self.goodSplit      = COLOUR['GREEN']
        self.badSplit       = COLOUR['RED']

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

    # Method sets font colour of split timers
    def setColour(self) -> None:
        if (self.timer < self.best):
            self.splits[self.index].setColour(self.goodSplit)
        elif (self.timer > self.best):
            self.splits[self.index].setColour(self.badSplit)                  

    # Method handles button press - if Select start/stop split timers
    def buttonPressed(self, button: int):
        if button == SELECT:
            if self.index < len(self.splits) - 1:
                if not self.timing:
                    self.timing = True
                    self.overall.startTimer()
                else:
                    self.timer = self.splits[self.index].getTimer(False)
                    self.best  = self.splits[self.index].getBest()
                    if (self.timer < self.best or self.best == "00:00"):
                        self.splits[self.index].setBest(self.timer)
                    self.setColour()
                    self.splits[self.index].stopTimer()
                    self.index = self.index + 1
                self.splits[self.index].startTimer()
            else:
                if (self.timer < self.best or self.best == "00:00"):
                    self.splits[self.index].setBest(self.timer)
                overallTimer = self.overall.getTimer(True)
                if (overallTimer < self.overallBest):
                    self.overallBest = overallTimer
                self.setColour()
                self.overall.stopTimer()
                self.splits[self.index].stopTimer()
                self.storeSplits()

    # Method sets defaults
    def setDefaults(self) -> None:
        self.overall = None
        self.splits  = []
        self.timing  = False
        self.index   = 0

    # Method restarts timer
    def restartTimer(self) -> None:
        self.setDefaults()
        self.chooseGame()
        self.setupGUI()

    # Method handles resetting of timer
    def resetTimer(self) -> None:
        self.attempts = "%03d" % (int(self.attempts) + 1)
        self.storeSplits()
        self.setDefaults()
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

        # Overall best
        token            = tokenizer.getToken()
        self.overallBest = token

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
            best = token[index + 1:]

            # Append split
            split = Split(self.screen, self.directory)
            split.setupSplit(image, label, best, \
                             self.adminFont, self.game)
            self.splits.append(split)

    # Method rewrites splits to file
    def storeSplits(self) -> None:
        tempSplits = []        
        path       = self.directory + "/files/splits/"
        
        if self.game == LOST_LEVELS:
            file = "lostlevels"
            
        fileObj = FileHandler(path, file)
        
        tempSplits.append(self.attempts)
        tempSplits.append(self.overallBest)
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
                colour = split.getColour()
                timer  = split.getTimer(False)
                best   = split.getBest()
                timerText = self.font.render(timer, 0, colour)
                self.screen.blit(timerText, (timerX, timerY))
                timerY = timerY + 30

        # Overall
        overallText = self.font.render(self.overall.getTimer(True), \
                                       0, self.adminFont)
        self.screen.blit(overallText, (48, 598))

        overallBestText = self.font.render(self.overallBest, \
                                           0, self.normalFont)
        self.screen.blit(overallBestText, (48, 616))
        

    
