import constants
import re
import Connect
import ConfigLoader

class WindowManager:
    global connection
    global config
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
        # Save the first port to use
        self.startingPort = config.get_conf_section_attribute(constants.CONFIG_FILE_VNC_SERVER_SECTION, "startingport")
        self.maxWindows = config.get_conf_section_attribute(constants.CONFIG_FILE_VNC_SERVER_SECTION, "maxwindows")
        self.usedPorts = [False] * self.maxWindows

    def openVNCServer(self, appId):
        """Creates a new VNC Server of the specified server appId"""
        # Find the first free port
        freePorts = [i for i, x in enumerate(self.usedPorts) if x]
        if len(freePorts) == 0: #if no ports are available
            raise Exception
        
        #now I have to manage multiwindows. need Connect to implement screen.
        
    
    def getWindowsList(self):
        """Returns the list of opened windows in the connected host"""
        regexp = re.compile(constants.REGEX_LIST_APP_COMMAND)
        #Send the command
        terminalResponse = self.connection.performCommand(constants.LIST_APP_COMMAND)
        #Decode matches in array 
        matches = regexp.findall(terminalResponse)
        #Transform it in a list of dicts
        toReturn = []
        for match in matches:
            toReturn.append({'id': match[0], 'name': match[1]})
        #Return matches as dict
        return toReturn
