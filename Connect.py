from pexpect import pxssh
from storm.parsers.ssh_config_parser import ConfigParser as StormParser
import constants


class Connect:
    # Handler for the view
    global view
    # Handler for the server ip
    global ip
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
            self.ip = connectionOptions['hostname']
            self.ssh.login(self.ip, connectionOptions['user'])
            #setting the virtual terminal size (for curses-designed scripts)
            #self.ssh.setwinsize(190, 90)

            #create temp dir for logs
            self.performCommand(constants.NEWDIR_TMP_LOG)
            #start screen on remote
            #self.performCommand("screen", usescreen = False)
            #self.ssh.sendline()


        except pxssh.ExceptionPxssh as err:
            raise err
    
    def __del__(self):
        """Simply logouts the connection"""
        self.ssh.logout()
        print("Connection closed")

    #def performCommand(self, command, usescreen = True, terminal = 0):
    def performCommand(self, command):
        """Performs a specified command to the connected host and returns the terminal response"""
        self.ssh.prompt(1)
        #Send the command to host
        # if usescreen:
        #     self.ssh.sendcontrol('a')
        #     self.ssh.send(str(terminal))
        #     #self.ssh.prompt()
        self.ssh.sendline(command)
        self.ssh.prompt(1)
        #Trigger the response string and return it
        #self.ssh.expect(pxssh.EOF)
        return self.ssh.before.decode("utf-8")
