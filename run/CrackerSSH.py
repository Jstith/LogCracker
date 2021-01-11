import re
from natsort import natsorted


class CrackerSSH():
    # Initialization of the object
    def __init__(self, args):
        # Public Variables
        self.__log_file = args.log
        self.__log_type = args.log_type
        self.__server_name = ""
        self.__succ_attempts = []
        self.__fail_attempts = []
        self.__ips = []
        self.__file_data = []

        # Try to read each line of the file into a different index in the list
        try:
            with open(self.__log_file, 'r') as reader:
                for line in reader:
                    self.__file_data.append(line)
        except Exception as e:
            print(f"Error: {e}")

    # Gathers information about the log
    def run_analysis(self):
        # Grabs the server hostname from the first line
        self.__server_name = self.__file_data[0].split(" ")[3]
        self.get_ip()
        self.__fail_attempts, self.__succ_attempts = self.attempts()

    # Extracts every IP from the time
    def get_ip(self):
        ips = []
        print("IP Addresses (sorted numerically):\n")
        # For every line check if IPs are present. If so, add them to ip list
        for line in self.__file_data:
            for ip in re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line):
                ips.append(ip)
        
        # Sort the IPs based on their numerical values
        self.__ips = natsorted(ips)

    # Find the successful and failed attempts
    def attempts(self):
        failed = []
        success = []
        for line in self.__file_data:
            if "Failed password" in line:
                current = line.split(" ")
                failed.append([current[8], current[10], current[12]])
            elif "Accepted password" in line:
                current = line.split(" ")
                success.append([current[8], current[10], current[12]])
        return failed, success


    # Prints useful data found in the file
    def print_info(self):
        print("\n__________ RESULTS __________\n")
        print("\tLog name: ", self.__log_file, "\n")
        print("\t\Log type: SSH\n")
        print("___________________ SERVER DETAILS ______________\n")
        print(f"\tSERVER NAMES: {self.__server_name}")
        print("\n__________ IPS ____________\n")
        print(*self.__ips, sep='\n')
        print()
        print(f"\n____________ FAILED CONNECTIONS: {len(self.__fail_attempts)} ______________\n")
        for each in self.__fail_attempts:
            print(f"\tUser: {each[0]}, IP: {each[1]}, PORT: {each[2]}")
        print(f"\n____________ SUCCESSFUL CONNECTIONS: {len(self.__succ_attempts)} ______________\n")
        for each in self.__succ_attempts:
            print(f"\tUser: {each[0]}, IP: {each[1]}, PORT: {each[2]}")
        print("\n____________________ END OF RESULTS_________________\n\n")    
