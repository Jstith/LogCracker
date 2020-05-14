import os
import re
import subprocess


class CrackerSSH():

    def __init__(self, args):
        self.__args = args
        __inFile = open(args[1])
        __line = __inFile.readline()
        __inFile.close()
        if(self.userCheck() and self.formatCheck(__line)):
            self.isSSH = True
            self.run()
        else:
            self.isSSH = False


    def userCheck(self):
        if(len(self.__args) >= 4):
            for x in range(len(self.__args)):
                if self.__args[x] == "-type":
                    if self.__args[x+1] != "SSH":
                        print("log type is not SSH")
                        return False
        return True


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


    def didItRun(self):
        return self.isSSH


    def run(self):

        self.__port = 0
        self.__serverName = ''
        self.__successfulLogins = 0

        print()

        __inFile = open(self.__args[1])
        for line in __inFile:
            __arr = line.split()
            if self.formatCheck(line):
                self.__serverName = __arr[3]
            if "Server listening" in line:
                self.__port = int(__arr[len(__arr)-1][:-1])
            if "Accepted password" in line:
                self.__successfulLogins += 1
        
        


    def getInfo(self):
        print("\n__________ Log Cracker __________\n")
        print("Log name:\n\n", self.__args[1], "\n")
        print("Log type:\tSSH\n")
        print("IP Addresses:\n")
        subprocess.call('chmod 755 scripts/ipCounter.sh', shell = True)
        subprocess.check_call(['scripts/ipCounter.sh', self.__args[1]])
        print()
        print("SSH is running on port:\t", end ='')
        print(self.__port)
        print("SSH server name is:\t", end ='')
        print(self.__serverName)
        print("Sucessful user logins:\t", end='')
        print(self.__successfulLogins)