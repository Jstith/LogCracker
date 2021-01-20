#! /usr/bin/python3
import argparse
from CrackerSSH import CrackerSSH
from CrackerGeneric import CrackerGeneric

# Supported log formats
supported_log_type = ["generic", "ssh"]

def main(args):
    # Check what type log the file is
    if(args.log_type == "ssh"):
        ssh = CrackerSSH(args)
        ssh.run_analysis()
        ssh.sort_attempts()
        if not args.quiet:
            ssh.generate_reports()
        if args.commands:
            ssh.search_commands()
        if args.search != None and args.search_term != None:
            ssh.search(args.search, args.search_term)
        ssh.print_info()
        if args.output != '' and args.output != None:
            try:
                ssh.write_to_file(args.output)
            except Exception as e:
                return 1
    else:
        CrackerGeneric(args)
    return 0   

# This functions grabs the arguments passed by the user
def collectArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='log', help='Inputed log', required=True)
    parser.add_argument('-t', '--type', dest='log_type', help='Log format, Supported formats include {}'.format(", ".join(supported_log_type)))
    parser.add_argument('-o', '--output', dest='output', help='Print formated results to file.')
    parser.add_argument('-s', '--search', dest='search', help = "Feature to search: user, port, or IP")
    parser.add_argument('-st', '--search-term', dest='search_term', help='Terms you want to search by separated by a single comma.')
    parser.add_argument('-q', '--quiet', action='store_true', help = 'Silences full report output. However, specific search term results will still show.')
    parser.add_argument('-c', '--commands', action='store_true', help='Search for commands logged')
    options = parser.parse_args()
    return options


if __name__ == '__main__':
    
    # Arguments passed by the user
    current_args = collectArguments()
    
    # Creates Object for the log passed by the user.
    current_log = main(current_args)
    user_input = input('Was the file successfully analyzed (Y/n): ')
    if user_input.lower() != 'y' and user_input != '':
        print("\nPlease start an issue at \"https://github.com/Jstith/LogCracker\"\n")
    else:
        print("\nGreat, Hopefully you find what you're looking for!!!\n")
        
