########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# App class: App initializer                                           #
#                                                                      #
# Created on 2017-2-3                                                  #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   .Constants    import *          # Constants file
from   .controllers  import NES, N64   # Controllers package
from   pygame.locals import *          # For key presses
import pygame                          # For GUI

########################################################################
#                                                                      #
#                               APP CLASS                              #
#                                                                      #
########################################################################

class Visualizer(object):
    screenHint = "Pygame screen"
    
    def __init__(self, screen: screenHint, appDirectory: str) -> None:
        self.screen       = screen
        self.appDirectory = appDirectory
        self.exists       = True   # Assume controller exists

        self.rectangle = (10, 652, 200, 128)
        self.offset    = (0, 0)

        # Set up GUI
        self.setTheme(STANDARD)
        self.setupGUI()

    # Method sets theme
    def setTheme(self, theme: int) -> None:
        self.rectangleColor = BLOCK[theme]

    # Mehtod sets up GUI
    def setupGUI(self) -> None:
        try:
            pygame.joystick.init()
            self.gamepad = pygame.joystick.Joystick(0)
            self.gamepad.init()
            name = self.gamepad.get_name()
            

            # Decide which controller to show
            if name == NES_NAME:        
                directory = self.appDirectory + NES_IMAGE_PATH
                self.controller = NES(name, directory)
                self.controllerImg = pygame.image.load(self.controller.getImage())
                self.pos = POS_NES
                            
            elif name == N64_NAME:        
                directory = self.appDirectory + N64_IMAGE_PATH
                self.controller = N64(name, directory)
                self.controllerImg = pygame.image.load(self.controller.getImage())
                self.pos = POS_N64

            # Load controller images
            self.images = self.controller.loadImages()
            if name == N64_NAME:
                stickImg    = self.controller.getStickImage()
                self.stick  = pygame.image.load(stickImg)
        except:
            self.exists = False

        # Visualizer screen
        self.visualizerRect = pygame.draw.rect(self.screen,         \
                                               self.rectangleColor, \
                                               self.rectangle)

    # Get controller type: NES or N64
    def getType(self) -> str:
        return self.controller.getType()

    # Handle button presses
    def buttonPressed(self, button: int) -> None:
        self.controller.buttonPressed(button)        

    # Handle button releases
    def buttonReleased(self, button: int) -> None:
        self.controller.buttonReleased(button)

    # Handle axis motion
    def axisMotion(self, axis: int, motion: int) -> (int, int):
        self.offset = self.controller.axisMotion(axis, motion)

    # Update controller visualizer: Display what buttons are pressed and
    # axis motions
    def update(self) -> None:# Visualizer screen
        self.visualizerRect = pygame.draw.rect(self.screen,         \
                                               self.rectangleColor, \
                                               self.rectangle)
        
        if self.exists:
            # Display controller with buttons pressed
            self.screen.blit(self.controllerImg, self.pos)
            self.visible = self.controller.getVisibleImages()
            for i in range(len(self.images)):
                if (self.visible[i]):
                    image = pygame.image.load(self.images[i])
                    self.screen.blit(image, self.pos)

            # N64 stick
            if (self.controller.getType() == "N64"):
                x = self.pos[ZERO] + self.offset[ZERO]
                y = self.pos[ONE]  + self.offset[ONE]
                pos = (x, y)
                self.screen.blit(self.stick, pos)    
