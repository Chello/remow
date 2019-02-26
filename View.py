import getpass

class View:

    def __init__(self):
        pass
    
    def send(self, toPrint):
        print(toPrint)

    def recieve(self, toRequest):
        return input(toRequest)

    def recievePassword(self, toRequest):
        return getpass.getpass(toRequest)

    def printAppList(self, appList):
        print("Choose one of these app:")
        i = 0
        for app in appList:
            print(i, ") ", app.name)
        return input("Choose an app: ")