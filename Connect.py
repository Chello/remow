from pexpect import pxssh
from storm.parsers.ssh_config_parser import ConfigParser as StormParser
import getpass

class Connect:
    def __init__(self):
        print("ciao")

    def connectionTests(self):
        try:                                                            
            s = pxssh.pxssh(options={
                "HostName": "192.168.0.100",
                "Port": "1296",
                "IdentityFile": "/home/chello/.ssh/chelloATNustrake",
                "User": "chello",
                "ForwardX11": "yes"
            })
            #hostname = input('hostname: ')
            #username = input('username: ')
            #password = getpass.getpass('password: ')
            s.login("192.168.0.100", "chello")
            s.sendline ('uptime')  # run a command
            s.prompt()             # match the prompt
            toPrint = s.before.decode("utf-8").replace("\r\n", "\n")
            print(type(str(s.before)))
            print(toPrint, "\n\n")
            # s.sendline ('ls -l')
            # s.prompt()
            # print(repr(s.before))
            # s.sendline ('df')
            # s.prompt()
            # print(repr(s.before))
            s.logout()
        except pxssh.ExceptionPxssh:
            print("pxssh failed on login.")
    
    def test(self):
        print("ciao")
