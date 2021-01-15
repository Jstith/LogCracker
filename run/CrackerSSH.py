import re
from natsort import natsorted
class CrackerSSH():
    
    # Initialization of the object
    def __init__(self, args):
        
        # Class level Variables
        self.__log_file = args.log
        self.__log_type = args.log_type
        self.__server_name = ""
        self.__succ_attempts = []
        self.__fail_attempts = []
        # self.__ips = []
        self.__file_data = []
        self.__report = []

        # Try to read each line of the file into a different index in the list
        try:
            with open(self.__log_file, 'r') as reader:
                for line in reader:
                    self.__file_data.append(line.replace("  ", " "))
        except Exception as e:
            print(f"Error: {e}")

    # Gathers information about the log
    def run_analysis(self):
        
        # Grabs the server hostname from the first line
        self.__server_name = self.__file_data[0].split(" ")[3]
        #self.get_ip()
        self.__fail_attempts, self.__succ_attempts = self.attempts()

    # # Extracts every IP from the time
    # def get_ip(self):
    #     ips = []
    #     # For every line check if IPs are present. If so, add them to ip list
    #     for line in self.__file_data:
    #         for ip in re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', line):
    #             ips.append(ip)
        
    #     Sort the IPs based on their numerical values
    #     self.__ips = natsorted(ips)

    # Find the successful and failed attempts
    def attempts(self):
        failed = []
        success = []
        for line in self.__file_data:
            if "Failed password" in line and "message repeated" not in line:
                current = line.split(" ")
                failed.append([current[len(current)-6], current[len(current)-4], current[len(current)-2]])
            elif ("Accepted password" in line or "Accepted publickey" in line) and "message repeated" not in line:
                current = line.split(" ")
                success.append([current[len(current)-6], current[len(current)-4], current[len(current)-2]])
        return failed, success



    # Sorts the number of attempts with the same IP, User, and port
    def sort_attempts(self):
        new_failed = []
        new_success = []
        # Find each unique attempt
        for each in self.__fail_attempts:
            if each not in new_failed:
                new_failed.append(each)
        for each in self.__succ_attempts:
            if each not in new_success:
                new_success.append(each)
        # Count each time the attempt occurred
        i = 0
        while i < len(new_failed):
            count = self.__fail_attempts.count(new_failed[i])
            new_failed[i].append(count)
            i+=1
        i = 0
        while i < len(new_success):
            count = self.__succ_attempts.count(new_success[i])
            new_success[i].append(count)
            i+=1
        
        self.__fail_attempts = new_failed
        self.__succ_attempts = new_success

    def generate_reports(self):
        self.__report.append("\n__________ RESULTS __________\n")
        self.__report.append(f"\tLog name: {self.__log_file}")
        self.__report.append("\tLog type: SSH\n")
        self.__report.append("___________________ SERVER DETAILS ______________\n")
        self.__report.append(f"\tSERVER NAMES: {self.__server_name}")
        self.__report.append(f"\n____________ FAILED CONNECTIONS: {len(self.__fail_attempts)} ______________\n")
        for each in self.__fail_attempts:
            self.__report.append(f"\tUser: {each[0]}, IP: {each[1]}, PORT: {each[2]}, TIMES: {each[3]}")
        self.__report.append(f"\n____________ SUCCESSFUL CONNECTIONS: {len(self.__succ_attempts)} ______________\n")
        for each in self.__succ_attempts:
            self.__report.append(f"\tUser: {each[0]}, IP: {each[1]}, PORT: {each[2]}, , TIMES: {each[3]}")
        self.__report.append("\n____________________ END OF RESULTS_________________\n\n")    

    
    # Prints useful data found in the file
    def print_info(self):
        for each_line in self.__report:
            print(each_line)
    

    # Prints results to file
    def write_to_file(self, filename):
        with open(filename, 'a+') as writer:
            for each_line in self.__report:
                writer.write(each_line + "\n")