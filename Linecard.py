import random

from Port import Port
from LinePerformance import LinePerformance
from UpTime import UpTime
import Constants
from LineDistance import Distance

perfms = ["Good","User","Bad", "Down", "NoSelt"]

class LineCard:
    def __init__(self,slot):
        self.slot = slot
        self.ports = {}
        for i in range(1,73):
            perm = random.choice(perfms)
            
            port = Port(LinePerformance(perm), UpTime())

            if not perm == "Down":
                port.enable()

            if perm == "NoSelt":
                port.disable()
                port.set_distance(Distance.PROBLEMATIC)

            self.ports[i] = port
            
    def getPort(self, port):
        if port in self.ports:
            return self.ports[port]

    def getLineStat(self, port):
        if port in self.ports:
            return self.ports[port].getLineStat(self.slot, port)
        
    def getLinerate(self, port):
        if port in self.ports:
            return self.ports[port].getLinerate(self.slot, port)

    def getDiagSeltTest(self, port):
        return self.ports[port].getDiagSeltTest(self.slot, port)
    
    def getDiagSeltShow(self, port):
        if port in self.ports:
            return self.ports[port].getDiagSeltShow(self.slot, port)
        
        
## TEST CODE ##
if __name__ == '__main__':
    print(Constants.LINE_STAT_HEADER)
    ln = LineCard(1)
    ln.getPort(10).enable()
    for i in range(1, 25):
        print(ln.getLineStat(i))

