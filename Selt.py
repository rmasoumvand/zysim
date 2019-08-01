class Selt:
    staus = """port\tinprogress\tcableType\tloopEstimateLength
    \r----\t--------\t--------\t------------------
    \r{}-{}\t {}\t\t{}\t\t{}m ({} kFT)"""

    def __init__(self):
        pass

    def doSeltTest(self, slot, port):
        pass

    def doSeltShow(self, slot, port, distance):
        import random
        area = random.choice(distance)

        if not area == "FAILED_START_LOOP_CHAR" or not area == "Failed":
            return self.staus.format(slot,port,"DONE","26AWG", area,area)
        else:
            return self.staus.format(slot, port, area, "24AWG", 0, 0)
