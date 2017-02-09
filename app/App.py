########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# App class: App initializer                                           #
#                                                                      #
# Created on 2016-12-29                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   .Constants    import *   # Constants file
from   .bot          import *   # Bot package
from   .visualizer   import *   # Controller visualizer package
from   .maingame     import *   # Main Game package
from   .cam          import *   # Web cam package
from   .splits       import *   # Splits package
from   .gameserver   import *   # Game server package
from   .info         import *   # Infom package
from   pygame.locals import *   # For Joystick listening
import pygame                   # For GUI
import time                     # For FPS

########################################################################
#                                                                      #
#                              APP CLASS                               #
#                                                                      #
########################################################################

class App(object):
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

        # Set up packages
        self.chatBlock  = ChatBlock(self.screen)
        self.visualizer = Visualizer(self.screen, self.appDirectory)
        self.game       = MainGame(self.screen)
        self.cam        = Cam(self.screen)
        self.splits     = Splits(self.screen, self.appDirectory)
        self.gameserver = GameServer(self.screen, self.appDirectory)
        self.info       = Info(self.screen, self.appDirectory)

    # Method sets app theme
    def setTheme(self, theme: int) -> None:
        self.chatBlock.setTheme(theme)
        self.visualizer.setTheme(theme)
        self.game.setTheme(theme)
        self.cam.setTheme(theme)
        self.splits.setTheme(theme)
        self.gameserver.setTheme(theme)
        self.info.setTheme(theme)
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
                    self.cam.close()
                    running = False

                # Handle right click event
                if event.type == pygame.MOUSEBUTTONDOWN and \
                   event.button == RIGHTCLICK:                    
                    theme = STANDARD
                    self.setTheme(theme)

                # Handle joystick button presses
                if (event.type == pygame.JOYBUTTONDOWN):
                    self.visualizer.buttonPressed(event.button)

                # Handle joystick button releases
                if (event.type == pygame.JOYBUTTONUP):
                    self.visualizer.buttonReleased(event.button)

                # Handle thumb stick
                if (event.type == JOYAXISMOTION):
                    # D-Pad on NES
                    if (self.visualizer.getType() == "NES"):
                        self.visualizer.axisMotion(event.axis, event.value)

                    # Stick on N64
                    elif (self.visualizer.getType() == "N64"):
                        self.visualizer.axisMotion(event.axis, event.value)

            # update application
            self.chatBlock.update()
            self.visualizer.update()
            self.game.update()
            self.cam.update()
            self.splits.update()
            self.gameserver.update()
            self.info.update()

            # Update Screen
            pygame.display.update()
            self.clock.tick(FPS)            

        # Close app cleanly
        pygame.quit()
