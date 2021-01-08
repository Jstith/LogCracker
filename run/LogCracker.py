#! /usr/bin/python3
import argparse
#import sys
from CrackerSSH import CrackerSSH
from CrackerGeneric import CrackerGeneric

supported_log_type = ["generic", "ssh"]

class LogCracker():
    
    """
    Currently supported formats:
    - SSH (development)
    - Generic (development)
    """

    def __init__(self, args):
        self.__args = args
        if(self.__args.log_type == "ssh"):
            ssh = CrackerSSH(self.__args)
            ssh.getInfo()
        else:
            CrackerGeneric(self.__args)

def collectArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='log', help='Inputed log', required=True)
    parser.add_argument('-t', '--type', dest='log_type', help='Log format, Supported formats include {}'.format(", ".join(supported_log_type)))
    options = parser.parse_args()
    return options


if __name__ == '__main__':
    args = collectArguments()
    LogCracker(args)