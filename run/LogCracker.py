import sys
import CrackerSSH
import CrackerGeneric

class LogCracker():
    
    """
    Currently supported formats:
    - SSH (development)
    - Generic (development)
    """

    __logTypes = ["generic, ssh"]

    def __init__(self, args):
        print(args)
        CrackerSSH.CrackerSSH(args)
        CrackerGeneric.CrackerGeneric(args)
    
    

if __name__ == '__main__':
    LogCracker(sys.argv)