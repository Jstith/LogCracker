import os
import re
import subprocess
from natsort import natsorted


class CrackerSSH():

    def __init__(self, args):
        self.__log_file = args.log
        self.__log_type = args.log_type
        file_data = []
        try:
            with open(self.__log_file, 'r') as reader:
                for line in reader:
                    file_data.append(line)
        except Exception as e:
            print(f"Error: {e.message}")
        self.__ips = self.getIPs(file_data)
        self.run()

    def run(self, file_arr):

        serverName = file_arr[0].split(" ")[3]
        successfulLogins = [login for login in file_arr if "Accepted password" in login]
        successfulLoginCount = len(successfulLogins)
        ips = self.getIPs(file_arr)
        print()

        # __inFile = open(self.__args.log)
        # for line in __inFile:
        #     __arr = line.split()
        #     if self.formatCheck(line):
        #         self.__serverName = __arr[3]
        #     if "Server listening" in line:
        #         self.__port = int(__arr[len(__arr)-1][:-1])
        #     if "Accepted password" in line:
        #         self.__successfulLoginCount += 1
        #         self.__successfulLogins += line

    def getIPs(self, file_arr):
        ips = []
        print("IP Addresses (sorted numerically):\n")
        for line in file_arr:
            for ip in re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line):
                ips.append(ip)
        ips = natsorted(ips)
        return ips



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
