########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Driver File                                                          #
#                                                                      #
# Created on 2016-12-27                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   app  import *   # Logger Class - Error logging
import os              # OS path

########################################################################
#                                                                      #
#                                DRIVER                                #
#                                                                      #
########################################################################

# Initialize app
def main():
    app = App(appDirectory)

# Store app directory
appDirectory = os.path.dirname(os.path.realpath(__file__))

# Initialize error logging
logger = Logger(appDirectory, 'w')

# Try to run app, otherwise log error
try:   
    main()
except:
    logger.createLog('')
