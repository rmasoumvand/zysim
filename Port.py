import sys
import Constants
from UpTime import UpTime
from LinePerformance import LinePerformance
from LineDistance import Distance
import time

class Port:
    def __init__(self, Performance, Uptime, Distance=Distance.NORMAL, Enabled=False):
        self.performance = Performance
        self.uptime = Uptime
        self.distance = Distance
        
        if not Enabled:
            self.uptime.disable() 
            self.type = "none"

        self.selt_start = 0
        self.enabled = Enabled

    def enable(self):
        self.enabled = True
        self.uptime.enable()
        self.type = Constants.ADSL2PLUS

    def disable(self):
        self.enabled = False
        self.uptime.disable()
        self.type = "none"

    def reset(self):
        self.disable()
        self.enable()
        
    
    def getStatus(self):
        return Constants.STATUS_UP if self.enabled else Constants.STATUS_DOWN

    def getLineStat(self,slot, port):
        return Constants.LINE_STAT_INFO.format(slot, port, self.getStatus(), self.performance.getLinePerformance(self.enabled)["actual_rate"][0], self.performance.getLinePerformance(self.enabled)["actual_rate"][1], self.type, self.uptime.getUpTime())


    def getLinerate(self, slot, port):
        perfm = self.performance.getLinePerformance(self.enabled)
        return Constants.LINE_RATE.format(slot, port, self.getStatus(), perfm["payload_rate"][0], perfm["payload_rate"][1], perfm["actual_rate"][0], perfm["actual_rate"][1], perfm["attainable_rate"][0], perfm["attainable_rate"][1], perfm["noise_margin"][0], perfm["noise_margin"][1], perfm["attenuation"][0], perfm["attenuation"][1])
        
    def getDiagSeltTest(self, slot, port):
        self.selt_start = time.time()

        
    def getDiagSeltShow(self, slot, port):
        if (self.distance == Distance.LONG):
            self.estimated_distance = '4300'
        elif (self.distance == Distance.NORMAL):
            self.estimated_distance = '1500'
        elif (self.distance == Distance.PROBLEMATIC):
            self.estimated_distance = '24'
        elif (self.distance == Distance.SHORT):
            self.estimated_distance = '120'

        if not self.selt_start == 0:
            if (int(time.time()) - int(self.selt_start)) >= 9:
                return Constants.DIAG_SELT_RESULT.format(slot, port, "DONE", "26AWG", Constants.DIAG_SELT_METER.format(self.estimated_distance, float(self.estimated_distance) * 0.032808))
            if (int(time.time()) - int(self.selt_start)) < 9 and (int(time.time()) - int(self.selt_start)) > 2:
                return Constants.DIAG_SELT_RESULT.format(slot, port, "FAILED_START_LOOP_CHAR", "24AWG",
                                                         Constants.DIAG_SELT_METER.format(self.estimated_distance,
                                                                                          float(
                                                                                              self.estimated_distance) * 0.032808))
        else:
            return Constants.DIAG_SELT_RESULT.format(slot, port, "START", "24AWG", Constants.DIAG_SELT_METER.format('0', 0.0))


    def set_distance(self, distance):
        self.distance = distance

## TEST CODE ##
if __name__ == '__main__':
    perfm = LinePerformance("Good")
    port = Port(perfm, UpTime(), Distance.LONG, Enabled=True)

    port.getDiagSeltTest(1,12)
    time.sleep(9)
    print(port.getDiagSeltShow(1,12))
