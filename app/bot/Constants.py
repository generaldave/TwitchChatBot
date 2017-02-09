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

SCREEN_RESOLUTION = (1918, 1004)
SCREEN_WIDTH      = 1918
SCREEN_HEIGHT     = 1004
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

########################################################################
#                                                                      #
#                            BOT CONSTANTS                             #
#                                                                      #
########################################################################

PROFANITY       = ["ass", "fuck", "bitch", "hell", "damn", "dam", \
                   "shit", "fucker", "fucking", "fucken", "asshole"]
GREETINGS       = ["hello", "hi", "hey", "yo", "greetings"]
CARRIAGE_RETURN = "\r\n"
BUFFER          = 1024

########################################################################
#                                                                      #
#                           8BALL CONSTANTS                            #
#                                                                      #
########################################################################

EIGHT_BALL =[]
EIGHT_BALL.append("It is certain.")
EIGHT_BALL.append("It is decidely so.")
EIGHT_BALL.append("Without a doubt.")
EIGHT_BALL.append("Yes, definitely.")
EIGHT_BALL.append("You may rely on it.")
EIGHT_BALL.append("As I see it, yes.")
EIGHT_BALL.append("Most Likely.")
EIGHT_BALL.append("outlook good.")
EIGHT_BALL.append("Yes.")
EIGHT_BALL.append("Signs point to yes.")
EIGHT_BALL.append("Reply hazy. Try again.")
EIGHT_BALL.append("Ask again later.")
EIGHT_BALL.append("Better not tell you now.")
EIGHT_BALL.append("Cannot predict now.")
EIGHT_BALL.append("Concentrate and ask again.")
EIGHT_BALL.append("Don't count on it.")
EIGHT_BALL.append("My reply is no.")
EIGHT_BALL.append("My sources say no.")
EIGHT_BALL.append("Outlook not so good.")
EIGHT_BALL.append("Very doubtful.")
