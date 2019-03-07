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
            self.performCommand(constants.NEWDIR_TMP_LOG, usescreen = False)
            #start screen on remote
            self.ssh.setwinsize(190, 90)
            self.performCommand("screen", usescreen = False)
            self.ssh.sendline()


        except pxssh.ExceptionPxssh as err:
            raise err
    
    def __del__(self):
        """Simply logouts the connection"""
        self.ssh.logout()
        print("Connection closed")

    def performCommand(self, command, usescreen = True, terminal = 0):
        """Performs a specified command to the connected host and returns the terminal response"""
        #Send the command to host
        if usescreen:
            self.ssh.sendcontrol('a')
            self.ssh.sendline(str(terminal))
        self.ssh.sendline(constants.LIST_APP_COMMAND)
        self.ssh.prompt()
        #Trigger the response string and return it
        #self.ssh.expect(pxssh.EOF)
        return self.ssh.before.decode("utf-8")
