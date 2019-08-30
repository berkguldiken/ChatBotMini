import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        

    def flush(self):
        
        pass    

    def start():
        sys.stdout = Logger()     
            
    def stop(self):
        self.log.write("-----")
        sys.stdout.logfile.close()
        sys.stdout = sys.stdout.terminal
    
