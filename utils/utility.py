import json,subprocess
from colorama import Fore, Style

class Utility(object):
    def typeChecker(self, obj, tp):
        return type(obj) == tp

    def readConfig(self, file) -> dict:
        with open(file, 'r') as config:
            content: dict = json.load(config)
            return content

    def saveConfig(self, file, object):
        with open(file, 'w') as config:
            json.dump(object, config, indent=4)

    def getNodeName(self,name: str):
        return "-".join(name.lower().split(" "))
    def getCriticalMessage(self,msg):
        return Fore.RED + f"Critical : {msg}" + Style.RESET_ALL

    def getNormalMessage(self,msg):
        return Fore.GREEN + msg + Style.RESET_ALL
    def getWarningMessage(self,msg):
        return Fore.YELLOW + f"Warn : {msg}" + Style.RESET_ALL

    def getSpecialMessage(self,msg):
        return Fore.MAGENTA + msg + Style.RESET_ALL

    def checkInstanceNameNotInUse(self,name) -> bool:
        hit = True
        '''
        Slice 0 index value : 0 index result of command is index of column
        '''
        for i in map(lambda x: x.split(),
                     subprocess.run(["multipass", "list"], stdout=subprocess.PIPE)
                             .stdout.decode('utf-8')
                             .split("\n")[1:]):
            try:
                if i[0] == name:
                    hit = False
                    break
            except:
                continue
        return hit