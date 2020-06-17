#!/usr/bin/env python3.7
import hashlib, sha3, sys

class Sha3(object):
    s = hashlib.sha3_512()
    arg = ""
    sha3arg = ""
    
    def setArg(self, _arg):
        self.arg = _arg.encode()

    def hashArg(self):
        self.s.update(self.arg)
        self.sha3arg = self.s.hexdigest()

    def getHashedArg(self):
        return self.sha3arg