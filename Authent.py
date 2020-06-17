from Sha3 import *

class Authent(object):
    shaLib = Sha3()

    def checkLogin(self, _user, _passwd):
        self.shaLib.setArg(_passwd)
        self.shaLib.hashArg()
        # print(self.shaLib.getHashedArg())
        if _user == "toto" and self.shaLib.getHashedArg() == "807d69324db83c874df0dd0d762e27351ebfedde58c72e40b4187dcbbdd46f15dacd14e1a369bc12deb21c5f1ab1a10ba7a3eef47feb9a939502377c5c0dda95":
            return True
        else:
            return False