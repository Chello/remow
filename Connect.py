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
        """Constructor
        Requests for connectionOptions object with connection details
        It connects to the host specified and keeps the connection opened
        """
        self.view = view
        try:                                                            
            self.ssh = pxssh.pxssh(options = connectionOptions)
            self.ssh.login(connectionOptions['hostname'], connectionOptions['user'])
            #self.ssh.sendline ('uptime')  # run a command
            #self.ssh.prompt()             # match the prompt
            #toPrint = self.ssh.before.decode("utf-8").replace("\r\n", "\n")
            #print(type(str(self.ssh.before)))
            #print(toPrint, "\n\n")

        except pxssh.ExceptionPxssh:
            print("pxssh failed on login.")
    
    def __del__(self):
        """Simply logouts the connection"""
        self.ssh.logout()

    def getWindowsList(self):
        """Returns the list of opened windows in the connected host"""
        regexp = re.compile(constants.REGEX_LIST_APP_COMMAND)
        #Send the command to host
        self.ssh.sendline(constants.LIST_APP_COMMAND)
        self.ssh.prompt()
        #Trigger the response string
        terminalResponse = self.ssh.before.decode("utf-8")
        #Decode matches in array 
        matches = regexp.findall(terminalResponse)
        #Transform it in a list of dicts
        toReturn = []
        for match in matches:
            toReturn.append({'id': match[0], 'name': match[1]})
        #Return matches as dict
        return toReturn
        