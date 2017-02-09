########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Cam Class: Block for web cam                                         #
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
import pygame.camera         # For webcam

########################################################################
#                                                                      #
#                              CAM CLASS                               #
#                                                                      #
########################################################################

class Cam(object):
    screenHint = "Pygame screen"
    
    def __init__(self, screen: screenHint) -> None:
        self.screen = screen

        self.rectangle = (10, 10, 200, 200)
        pygame.camera.init()
        self.camera = pygame.camera.Camera(pygame.camera.list_cameras()[0])
        

        self.setTheme(STANDARD)
        self.setupGUI()

    # Method sets theme
    def setTheme(self, theme: int) -> None:
        self.rectangleColor = BLOCK[theme]

    # Method updates web cam block
    def setupGUI(self) -> None:
        self.camRect = pygame.draw.rect(self.screen, self.rectangleColor,
                                         self.rectangle)
        self.camera.start()

    # Method updates Cam block
    def update(self) -> None:
        image = self.camera.get_image()
        image = pygame.transform.scale(image, (200, 200))
        self.screen.blit(image, self.camRect)

    # Method closes camera
    def close(self) -> None:
        self.camera.stop()
        
        
