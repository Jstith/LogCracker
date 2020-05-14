import subprocess

subprocess.call('chmod 755 test.sh', shell = True)
subprocess.check_call(['./test.sh', "Hello there"])