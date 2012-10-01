import argparse

from contactpoint import ContactPoint
from env import shud_i_debug

# Init ContactPoint
CP = ContactPoint(shud_i_debug)
CP.listen()

app = CP.server

'''
This initializes the application
'''
if __name__ == "__main__":
    port = 8008

    '''
    Better command line argument parsing
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', help='Run the application using the port specified', type=int)
    args = parser.parse_args()
    if args.port:
        port = args.port

    try:
        app.listen(port)
    except KeyboardInterrupt:
        CP.logger.log('Server forced closed by user.')