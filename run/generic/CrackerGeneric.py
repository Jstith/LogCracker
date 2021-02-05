class CrackerGeneric():
    
         # Initialization of the object
    def __init__(self, args):
        
        # Class level Variables
        self.__log_file = args.log
        self.__file_data = []
        self.report = []

        # Try to read each line of the file into a different index in the list
        try:
            with open(self.__log_file, 'r') as reader:
                for line in reader:
                    self.__file_data.append(line.replace("  ", " "))
        except Exception as e:
            print(f"Error: {e}")

    # Prints useful data found in the file
    def print_info(self):
        for each_line in self.report:
            print(each_line)

    # Prints results to file
    def write_to_file(self, filename):
        with open(filename, 'a+') as writer:
            for each_line in self.report:
                writer.write(each_line + "\n")