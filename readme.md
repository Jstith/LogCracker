__LogCracker__
===============

![LogCracker Logo](resources/logcracker.png)

By: _Jstith_ and _Soups71_

## Usage

```
usage: LogCracker.py [-h] -f LOG [-t LOG_TYPE] [-o OUTPUT] [-s SEARCH] [-st SEARCH_TERM] [-q] [-c]

optional arguments:
  -h, --help            show this help message and exit
  -f LOG, --file LOG    Inputed log
  -t LOG_TYPE, --type LOG_TYPE
                        Log format, Supported formats include generic, ssh
  -o OUTPUT, --output OUTPUT
                        Print formated results to file.
  -s SEARCH, --search SEARCH
                        Feature to search: user, port, or IP
  -st SEARCH_TERM, --search-term SEARCH_TERM
                        Terms you want to search by separated by a single comma.
  -q, --quiet           Silences full report output. However, specific search term results will still show.
  -c, --commands        Search for commands logged
```

## The Idea

In my experience with log analysis in CTFs, I find myself always following a pattern. There many different types of logs, and there are many different things we get asked about logs, but ultimately I do the same thing every time with different data. LogCracker is an attempt to streamline that process and automate pulling information from log files. What I want this to do is identify the type of log it's given, pull out basic information about that log, and present the user options and scripts to get further information based on what they need to find.

## How it Works

There are several different ways to go about log analysis. LogCracker follows my personal methodology, and uses a python to manipulate the data in the log files.

## What works right now

Currently, you can run the python file with a log file passed as an argument and the program will try to identify what kind of log it is. Right now, the only working option is of ssh logs. If the log is an ssh log, it will parse through the log and display some basic information:
- Name of SSH server
- Attempted logons
- Successful logons
- Commands ran as root
- Search for specific user, IP, or port


![auth.log file example](resources/ssh_example.png)

## Future Goals

- More information about logs
- User specified information about logs
- Multiple types of logs
- Generic reader to get basic information about any format
- Easier access to the library of scripts
  - I don't want this to be purely a plug and chug program, but rather a library of scripts (python and bash) with some direction on how to use them in order to speed up the process... and a plug and chug option.
- A GUI.. of course
