import constants
import re
import Connect
import ConfigLoader
import os

class WindowManager:
    global connection
    global config
    global ip
    #the starting port
    global startingPort
    """the list of available/used ports
    Is a list of booleans and its meaning is that
        if usedPorts[0] then startingPort is used
        if not usedPOrt[1] then (startingPort + 1) is free
        and so on
    """
    global usedPorts
    #the max number of windows
    global maxWindows

    def __init__(self, connection, config):
        self.connection = connection
        self.config = config
        # save the IP
        self.ip = connection.ip
        # Save the first port to use
        self.startingPort = config.get_conf_section_attribute(constants.CONFIG_FILE_VNC_SERVER_SECTION, "startingport")
        self.maxWindows = int(config.get_conf_section_attribute(constants.CONFIG_FILE_VNC_SERVER_SECTION, "maxwindows"))
        self.usedPorts = [False] * self.maxWindows

    def openVNCServer(self, appId):
        """Creates a new VNC Server of the specified server appId.
        Returns the port in which responds the VN Server"""
        # Find the first free port
        # freePorts = [i for i, x in enumerate(self.usedPorts) if x]
        # if len(freePorts) == 0: #if no ports are available
        #     raise Exception
        
        self.connection.performCommand(constants.DE_MAXIMIZE_WINDOW(appId))

        width = self.config.get_conf_section_attribute(constants.CONFIG_FILE_VNC_SERVER_SECTION, "windowswidth")
        height = self.config.get_conf_section_attribute(constants.CONFIG_FILE_VNC_SERVER_SECTION, "windowsheight")
        self.connection.performCommand(constants.SET_WINDOW_SIZE(appId, width, height))
        
        self.connection.performCommand(constants.NEW_SERVER_ISTANCE(appId, self.startingPort))
        
        return self.startingPort
        #now I have to manage multiwindows. need Connect to implement screen.
    
    def openVNCClient(self, port):
        com = constants.NEW_CLIENT_ISTANCE(self.ip, port)
        print(com)
        os.system(com)

    
    def getWindowsList(self):
        """Returns the list of opened windows in the connected host"""
        regexp = re.compile(constants.REGEX_LIST_APP_COMMAND)
        #Send the command
        terminalResponse = self.connection.performCommand(constants.LIST_APP_COMMAND)
        print(terminalResponse)
        #Decode matches in array 
        matches = regexp.findall(terminalResponse)
        #Transform it in a list of dicts
        toReturn = []
        for match in matches:
            toReturn.append({'id': match[0], 'name': match[1]})
        #Return matches as dict
        return toReturn
