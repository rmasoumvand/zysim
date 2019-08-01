from Linecard import LineCard

class DSLAM:
    def __init__(self,slot):
        self.linecards = {}
        for i in range(1, int(slot)+1):
            linecard = LineCard(i)
            self.linecards[i] = linecard

    def getSlot(self, slot):
        if slot in self.linecards:
            return self.linecards[slot]
        
        
## TEST CODE ##
if __name__ == '__main__':
    dslam = DSLAM(7)
    dslam.getSlot(6).getPort(12).enable()
    print(dslam.getSlot(2).getLineStat(13))
    print(dslam.getSlot(6).getLineStat(12))
