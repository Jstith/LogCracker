class CrackerSSH():
    
    # Initialization of the object
    def __init__(self, args):
        
        # Class level Variables
        self.__log_file = args.log
        self.__log_type = args.log_type
        self.__server_name = ""
        self.__succ_attempts = []
        self.__fail_attempts = []
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
        self.__fail_attempts, self.__succ_attempts = self.attempts()

    # Find the successful and failed attempts
    def attempts(self):
        failed = []
        success = []
        for line in self.__file_data:
            if "sshd[" in line: 
                if "Failed" in line and "message repeated" not in line:
                    current = line.strip().split(" ")
                    failed.append([current[current.index("from")-1],
                                   current[current.index("port")-1], 
                                   current[current.index("port")+1]])
                elif ("Accepted" in line) and "message repeated" not in line:
                    current = line.strip().split(" ")
                    success.append([current[current.index("from")-1],
                                    current[current.index("port")-1],
                                    current[current.index("port")+1]])
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

    def search(self, item, keys):
        current_search = item
        items_to_find = keys.split(",")
        results = []
        Error = ""
        for search_term in items_to_find:
            count = 0
            if item == "user":
                for each_item in self.__fail_attempts:
                    if each_item[0] == search_term:
                        count += 1
                for each_item in self.__succ_attempts:
                    if each_item[0] == search_term:
                        count += 1    
            elif item == "port":
                for each_item in self.__fail_attempts:
                    if each_item[2] == search_term:
                        count += 1
                for each_item in self.__succ_attempts:
                    if each_item[2] == search_term:
                        count += 1    
            elif item == "ip":
                for each_item in self.__fail_attempts:
                    if each_item[1] == search_term:
                        count += 1
                for each_item in self.__succ_attempts:
                    if each_item[1] == search_term:
                        count += 1    
            else:
                # Do Nothin
                Error = "Please select proper search term"
                break
            results.append([search_term, count])
        self.__report.append(f"\n_______________ Specific Search: {' '.join(items_to_find)} _______________")
        if len(results) > 0:
            for each in results:
                self.__report.append(f'\t{current_search.capitalize()}: {each[0]}\tTimes: {each[1]}\n')
        else:
            self.__report.append(Error+"\n")
        self.__report.append(f"________________ End of Specific Search ________________\n")

    def search_commands(self):
        commands = []
        for line in self.__file_data:
            if "PWD" in line and "COMMAND" in line and "sudo" in line:
                line = ' '.join(line.split())
                line_arr = line.split(" ")
                commands.append([line_arr[line_arr.index("sudo:")+1], 
                                line[line.index("PWD")+4:].split(" ")[0],
                                line[line.index("COMMAND=")+len("COMMAND="):]])
        self.__report.append("\n______________ SUDO HISTORY _______________")
        for each in commands:
             self.__report.append(f"User: {each[0]}; Directory ran in: {each[1]}; Command ran: {each[2]}\n")
        self.__report.append("______________ END of SUDO HISTORY _______________\n")



    def generate_reports(self):
        self.__report.append("\n__________ BASIC RESULTS __________\n")
        self.__report.append(f"\tLog name: {self.__log_file}")
        self.__report.append("\tLog type: SSH\n")
        self.__report.append("___________________ SERVER DETAILS ______________\n")
        self.__report.append(f"\tSERVER NAME: {self.__server_name}")
        self.__report.append(f"\n____________ FAILED CONNECTIONS: {len(self.__fail_attempts)} ______________\n")
        for each in self.__fail_attempts:
            self.__report.append(f"\tUser: {each[0]}, IP: {each[1]}, PORT: {each[2]}, TIMES: {each[3]}")
        self.__report.append(f"\n____________ SUCCESSFUL CONNECTIONS: {len(self.__succ_attempts)} ______________\n")
        for each in self.__succ_attempts:
            self.__report.append(f"\tUser: {each[0]}, IP: {each[1]}, PORT: {each[2]}, , TIMES: {each[3]}")
        self.__report.append("\n____________________ END OF BASIC RESULTS_________________\n\n")    

    
    # Prints useful data found in the file
    def print_info(self):
        for each_line in self.__report:
            print(each_line)

    # Prints results to file
    def write_to_file(self, filename):
        with open(filename, 'a+') as writer:
            for each_line in self.__report:
                writer.write(each_line + "\n")