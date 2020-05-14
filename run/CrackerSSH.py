import regex

class CrackerSSH():

    def __init__(self, args):
        print("ssh init")
        self.__args = args
        if(self.userCheck() and self.formatCheck()):
            self.run()

    def userCheck(self):
        print("usercheck")
        if(len(self.__args) >= 4):
            for x in range(len(self.__args)):
                if self.__args[x] == "-type":
                    if self.__args[x+1] != "SSH":
                        print("log type is not SSH")
                        return False
        return True
    
    def formatCheck(self):
        print("formatcheck")
        __months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        __time = regex.compile(r'\d\d:\d\d:\d\d')

        __inFile = open(self.__args[1])
        for line in __inFile:
            __arr = line.split()
            if(__arr[0] in __months):
                print("1")
                if(__arr[1].isnumeric()):
                    print("2")
                    if(__time.match(__arr[2])):
                        print("3")
                        if("sshd" in __arr[4]):
                            print("4")
                            __inFile.close()
                            return True
        __inFile.close()
        return False



    def run(self):
        print("running SSH")
