import time

class Logger:
    
    '''The Logger class handles logging & displaying of debug messages''' 
    
    debugging = False
    LOG_PATH = 'instance/logs'
    
    def __init__(self, debugging = False):
        '''
        In debugging mode, the logs will be truncated each time the logger is
        booted.
        '''
        self.debugging = debugging
    
    def debug(self, msg = ''):
        '''
        Displays the provided message, if the app is running in the development
        environment(which is indicated by the debugging property).
        '''
        if msg == '':
            return
        if self.debugging is True:
            print msg
    
    def log(self, msg = ''):
        '''
        Logs the provided message and passes it on to debug mode to display the
        message.
        '''
        if msg == '':
            return
        with open(self.LOG_PATH, 'a+') as f:
            f.write(time.strftime('%x %X %Z ') + msg + '\n')
            f.close
        self.debug(msg)
