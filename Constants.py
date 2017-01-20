########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Constants file                                                       #
#                                                                      #
# Created on 2017-1-17                                                 #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          SCREEN ATTRIBUTES                           #
#                                                                      #
########################################################################

SCREEN_RESOLUTION = (350, 480)
SCREEN_WIDTH      = 350
SCREEN_HEIGHT     = 480
TITLE             = "Twitch Chat Bot"
FPS               = 60

########################################################################
#                                                                      #
#                          MOUSE ATTRIBUTES                            #
#                                                                      #
########################################################################

RIGHTCLICK = 3

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
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

# Path of Exile theme
LIGHTGRAY  = (30, 31, 30)
COPPER     = (163, 141, 109)
GOLD       = (219, 159, 0)

# Coding theme
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

# Retro Gaming theme
GRAY  = (200, 200, 200)

########################################################################
#                                                                      #
#                          THEME CONSTANTS                             #
#                                                                      #
########################################################################

STANDARD     = 0
PATHOFEXILE  = 1
CODING       = 2
RETROGAMING  = 3

#               Standard   Path of Exile   Coding   Retro Gaiming
BACKGROUND   = [BLACK,     WHITE,          GREEN,   BLACK]
BLOCK        = [WHITE,     LIGHTGRAY,      COPPER,  GRAY]
ADMIN_COLOUR = [RED,       GOLD,           BLUE,    WHITE]
TEXT_COLOUR  = [BLACK,     COPPER,         BLACK,   BLACK]

########################################################################
#                                                                      #
#                             BOT CONSTANTS                            #
#                                                                      #
########################################################################

PROFANITY       = ["ass", "fuck", "bitch", "hell", "damn", "dam",
                   "shit"]
CARRIAGE_RETURN = "\r\n"
BUFFER          = 1024
