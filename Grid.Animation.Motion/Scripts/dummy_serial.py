

class Serial:
    def __init__(self, verbose=False, *args, **kwargs):
        self.verbose = verbose
        self.report("Loading dummy serial port for testing purposes", args, kwargs)
    
    def report(self, *args, **kwargs):
        if self.verbose:
            print(args)
            print(kwargs)
    
    def write(self, *args, **kwargs):
        self.report(args, kwargs)
    
    def read(self, *args, **kwargs):
        self.report(args, kwargs)
    
    def sleep(self, *args, **kwargs):
        self.report(args, kwargs)
    
    def open(self, *args, **kwargs):
        self.report(args, kwargs)
    
    def close(self, *args, **kwargs):
        self.report(args, kwargs)
