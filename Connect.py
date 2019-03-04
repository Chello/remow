from pexpect import pxssh
from storm.parsers.ssh_config_parser import ConfigParser as StormParser
import constants


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

            #create temp dir for logs
            self.ssh.sendline(constants.NEWDIR_TMP_LOG)
            self.ssh.prompt()

        except pxssh.ExceptionPxssh as err:
            raise err
    
    def __del__(self):
        """Simply logouts the connection"""
        self.ssh.logout()
        print("Connection closed")

    def performCommand(self, command):
        """Performs a specified command to the connected host and returns the terminal response"""
        #Send the command to host
        self.ssh.sendline(constants.LIST_APP_COMMAND)
        self.ssh.prompt()
        #Trigger the response string and return it
        return self.ssh.before.decode("utf-8")