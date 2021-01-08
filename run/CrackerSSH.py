import os
import re
import subprocess
from natsort import natsorted


class CrackerSSH():

    def __init__(self, args):
        self.__args = args
        self.__ips = []
        self.run()

    def formatCheck(self, line):
        __months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        __time = re.compile(r'\d\d:\d\d:\d\d')

        __arr = line.split()
        if(__arr[0] in __months):
            if(__arr[1].isnumeric()):
                if(__time.match(__arr[2])):
                    if("sshd" in __arr[4]):
                        return True
        return False

    def run(self):

        self.__port = 0
        self.__serverName = ''
        self.__successfulLoginCount = 0
        self.__successfulLogins = ''

        print()

        __inFile = open(self.__args.log)
        for line in __inFile:
            __arr = line.split()
            if self.formatCheck(line):
                self.__serverName = __arr[3]
            if "Server listening" in line:
                self.__port = int(__arr[len(__arr)-1][:-1])
            if "Accepted password" in line:
                self.__successfulLoginCount += 1
                self.__successfulLogins += line

    def getIPs(self):
        ips = []
        print("IP Addresses (sorted numerically):\n")
        with open(self.__args.log, 'r') as reader:
            for line in reader:
                for ip in re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line):
                    ips.append(ip)
        self.__ips = natsorted(ips)


    def getInfo(self):
        print("\n__________ Log Cracker __________\n")
        print("Log name:\n\n", self.__args.log, "\n")
        print("Log type:\tSSH\n")
        self.getIPs()
        print(*self.__ips, sep='\n')
        # subprocess.call('chmod 755 scripts/ipCounter.sh', shell = True)
        # subprocess.check_call(['scripts/ipCounter.sh', self.__args.log])
        # print()
        # print("SSH is running on port:\t", end ='')
        # print(self.__port)
        # print("SSH server name is:\t", end ='')
        # print(self.__serverName)
        # print("Sucessful user logins:\t", end='')
        # print(self.__successfulLoginCount, "\n")
        # print(self.__successfulLogins)
