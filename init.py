########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# init class: App initializer                                          #
#                                                                      #
# Created on 2016-12-29                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Constants import *   # Constants file
from   ChatBlock import *   # Chat Block class
from   Bot       import *   # Twitch Bot class
import pygame               # For GUI
import time

########################################################################
#                                                                      #
#                              INIT CLASS                              #
#                                                                      #
########################################################################

class init(object):
    def __init__(self, appDirectory : str):
        self.appDirectory = appDirectory

        # Set up GUI
        self.setupGUI()

        # Initialize bot
        self.bot = Bot(self, self.appDirectory)
        self.bot.start()

        # Run app
        self.runApp()        

    # Mehtod sets up GUI
    def setupGUI(self):
        # Screen attributes
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RESOLUTION)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()      # For frames per second
        self.mouse = pygame.mouse.get_pos()   # For mouse position
        self.background = BACKGROUND[STANDARD]

        # Set up chat block
        self.chatBlock = ChatBlock(self.screen)

    # Method sets app theme
    def setTheme(self, theme: int) -> None:
        self.chatBlock.setTheme(theme)
        self.background = BACKGROUND[theme]

    # Method runs app
    def runApp(self):
        running = True
        while running:
            self.screen.fill(self.background)
            for event in pygame.event.get():
                # Handle quit event
                if event.type == pygame.QUIT:
                    self.bot.stop()
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and \
                   event.button == RIGHTCLICK:                    
                    theme = STANDARD
                    self.setTheme(theme)

            # update chat block
            self.chatBlock.update()

            # Update Screen
            pygame.display.update()
            self.clock.tick(FPS)            

        # Close app cleanly
        pygame.quit()
