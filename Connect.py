from pexpect import pxssh
from storm.parsers.ssh_config_parser import ConfigParser as StormParser
import constants
import re


class Connect:
    # Handler for the view
    global view

    # Handler for the ssh connection
    global ssh

    def __init__(self, connectionOptions, view):
        self.view = view
        try:                                                            
            self.ssh = pxssh.pxssh(options = connectionOptions)
            #     "HostName": "192.168.0.100",
            #     "Port": "1296",
            #     "IdentityFile": "/home/chello/.ssh/chelloATNustrake",
            #     "User": "chello",
            #     "ForwardX11": "yes"
            # })
            #hostname = input('hostname: ')
            #username = input('username: ')
            #password = getpass.getpass('password: ')
            #s.login("192.168.0.100", "chello")
            self.ssh.login(connectionOptions['hostname'], connectionOptions['user'])
            #self.ssh.sendline ('uptime')  # run a command
            #self.ssh.prompt()             # match the prompt
            #toPrint = self.ssh.before.decode("utf-8").replace("\r\n", "\n")
            #print(type(str(self.ssh.before)))
            #print(toPrint, "\n\n")

        except pxssh.ExceptionPxssh:
            print("pxssh failed on login.")
    
    def __del__(self):
        self.ssh.logout()

    def getWindowsList(self):
        regexp = re.compile(constants.REGEX_LIST_APP_COMMAND)
        self.ssh.sendline (constants.LIST_APP_COMMAND)  # run a command
        self.ssh.prompt()             # match the prompt
        terminalResponse = self.ssh.before.decode("utf-8").replace("\r\n", "\n")

        return regexp.findall(terminalResponse)
        # for (appId, appName) in re.findall(regexp, terminalResponse):
        #     print(appId, appName)
        # for row in rows:
        #     if row != constants.LIST_APP_COMMAND and len(row) != 0:
        #         m = re.match("(0x[0-9a-f]*)[ ]*[0-9\-]*[\s\t]*[^ ]*[ ]*(.*)", row)
        #         print(m.group(1), " ", m.group(2))