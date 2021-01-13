#! /usr/bin/python3
import argparse
from CrackerSSH import CrackerSSH
from CrackerGeneric import CrackerGeneric

# Supported log formats
supported_log_type = ["generic", "ssh"]

def main(args):
    
    # Check what type log the file is
    if(args.log_type == "ssh"):
        print('Running analysis as if the log is an SSH auth log')
        ssh = CrackerSSH(args)
        ssh.run_analysis()
        ssh.sort_attempts()
        ssh.generate_reports()
        ssh.print_info()
        if args.output != ''== None:
            try:
                ssh.write_to_file(args.output)
            except Exception as e:
                print(f"ERROR: {e}")
        user_input = input('Was the SSH file successfully analyzed (Y/n): ')
        if user_input.lower() != 'y' and user_input != '':
            return False
    else:
        print("Running Generic Log scan")
        CrackerGeneric(args)
        user_input = input('Was the file successfully analyzed (Y/n): ')
        if user_input.lower() != 'y' and user_input != '':
            return False
    return True    

# This functions grabs the arguments passed by the user
def collectArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='log', help='Inputed log', required=True)
    parser.add_argument('-t', '--type', dest='log_type', help='Log format, Supported formats include {}'.format(", ".join(supported_log_type)))
    parser.add_argument('-o', '--output', dest='output', help='Print formated results to file.')
    options = parser.parse_args()
    return options


if __name__ == '__main__':
    
    # Arguments passed by the user
    current_args = collectArguments()
    
    # Creates Object for the log passed by the user.
    current_log = main(current_args)
    if current_log:
        print("\nGreat, Hopefully you find what you're looking for!!!\n")
    else:
        print("\nPlease start an issue at \"https://github.com/Jstith/LogCracker\"\n")
