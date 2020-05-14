import re
import os
import subprocess

class CrackerSSH():

    def __init__(self, args):
        #print("ssh init")
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
        #print("usercheck")
        if(len(self.__args) >= 4):
            for x in range(len(self.__args)):
                if self.__args[x] == "-type":
                    if self.__args[x+1] != "SSH":
                        print("log type is not SSH")
                        return False
        return True


    def formatCheck(self, line):
        #print("formatcheck")
        __months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        __time = re.compile(r'\d\d:\d\d:\d\d')

        __arr = line.split()
        #print("__arr is", __arr)
        if(__arr[0] in __months):
            #print("1")
            if(__arr[1].isnumeric()):
                #print("2")
                if(__time.match(__arr[2])):
                    #print("3")
                    if("sshd" in __arr[4]):
                        #print("4")
                        return True
        return False


    def didItRun(self):
        return self.isSSH

    def run(self):
        
        print("\n__________ Log Cracker __________\n")
        print("Log name:\n\n", self.__args[1], "\n")
        print("Log type:\n\nSSH\n")
        print("IP Addresses:\n")

        __port = 0
        __serverName = ''
        __successfulLogins = 0

        subprocess.call('chmod 755 scripts/ipCounter.sh', shell = True)
        subprocess.check_call(['scripts/ipCounter.sh', self.__args[1]])

        print()

        #print("running SSH")
        __inFile = open(self.__args[1])
        for line in __inFile:
            __arr = line.split()
            #print("sending line", line)
            if self.formatCheck(line):
                __serverName = __arr[3]
            if "Server listening" in line:
                __port = int(__arr[len(__arr)-1][:-1])
            if "Accepted password" in line:
                __successfulLogins += 1
        
        print("SSH is running on port:\t", end ='')
        print(__port)
        print("SSH server name is:\t", end ='')
        print(__serverName)
        print("Sucessful user logins:\t", end='')
        print(__successfulLogins)