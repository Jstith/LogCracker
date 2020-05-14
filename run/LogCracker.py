#! /usr/bin/python3

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
        self.__args = args
        ssh = CrackerSSH.CrackerSSH(self.__args)
        if ssh.didItRun():
            ssh.getInfo()
        else:
            CrackerGeneric.CrackerGeneric(args)

if __name__ == '__main__':
    LogCracker(sys.argv)