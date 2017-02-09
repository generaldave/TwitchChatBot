########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Constants file                                                       #
#                                                                      #
# Created on 2017-2-3                                                  #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                        CONTROLLER CONSTANTS                          #
#                                                                      #
########################################################################

# NES
POS_NES  = (15, 675)
NES_NAME = "RetroUSB.com RetroPad"

# N64
POS_N64  = (46, 657)
N64_NAME = "SealieComputing N64 RetroPort"

########################################################################
#                                                                      #
#                           PATH CONSTANTS                             #
#                                                                      #
########################################################################

NES_IMAGE_PATH = "/images/nes/"
N64_IMAGE_PATH = "/images/n64/"

########################################################################
#                                                                      #
#                          NUMBER CONSTANTS                            #
#                                                                      #
########################################################################

ZERO = 0
ONE  = 1
TWO  = 2


########################################################################
#                                                                      #
#                          COLOUR CONSTANTS                            #
#                                                                      #
########################################################################

# Standard Theme
WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)
RED       = (255, 0, 0)

# Path of Exile theme
DARKGRAY  = (30, 31, 30)
COPPER    = (163, 141, 109)
GOLD      = (219, 159, 0)

# Coding theme
GREEN     = (0, 200, 25)
DARKBLUE  = (0, 0, 50)

# Retro Gaming theme
BLUE      = (0, 50, 255)
LIGHTGRAY = (150, 150, 150)

########################################################################
#                                                                      #
#                          THEME CONSTANTS                             #
#                                                                      #
########################################################################

STANDARD     = 0
PATHOFEXILE  = 1
CODING       = 2
RETROGAMING  = 3

#               Standard   Path of Exile   Coding       Retro Gaiming
BACKGROUND   = [BLACK,     BLACK,          BLACK,       DARKGRAY]
BLOCK        = [WHITE,     DARKGRAY,       DARKBLUE,    LIGHTGRAY]
ADMIN_COLOUR = [RED,       GOLD,           GREEN,       BLUE]
TEXT_COLOUR  = [BLACK,     COPPER,         WHITE,       WHITE]


