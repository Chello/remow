import constants
import re
import Connect

class WindowManager:
    global connection
    global configuration

    def __init__(self, connection, configuration):
        self.connection = connection
        self.configuration = configuration

    def openVNCServer(self, appId):
        pass
        
    
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
