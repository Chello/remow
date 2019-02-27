import getpass

class View:

    def __init__(self):
        pass
    
    def send(self, toPrint):
        print(toPrint)

    def recieveString(self, toRequest):
        return input(toRequest)

    def recievePassword(self, toRequest):
        return getpass.getpass(toRequest)

    def promptAppRequest(self, appList):
        """Requires the app list 
        The app list is composed of:
        [
            {'id', 'name'},
            ...
        ]
        Asks to choose the app
        Returns the dict of the app chosen
        """

        print("Choose one of these app:")
        i = 1
        for app in appList:
            print(i, ") \t", app['name'])
            i += 1
        return self.recieveValidAppElement(appList)
    
    def recieveInt(self, toDisplay, error = False):
        if error:
            self.send("Please type an integer.")
        try:
            return int(input(toDisplay))
        except ValueError:
            return self.recieveInt(toDisplay, True)

    def recieveValidAppElement(self, appList):
        try:
            return appList[self.recieveInt("Choose an app: ") -1]
        except IndexError:
            self.send("Please type a correct value.")
            return self.recieveValidAppElement(appList)
