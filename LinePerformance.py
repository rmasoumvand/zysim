class LinePerformance:
    performance = {
        "Good" : {
            "payload_rate" : (999,23000),
            "actual_rate" : (1008,29000),
            "attainable_rate" : (1008, 29000),
            "noise_margin": (18.8,24.0),
            "attenuation" : (1.5, 3.0)
        },

        "User" : {
            "payload_rate": (999, 13000),
            "actual_rate": (1008, 13000),
            "attainable_rate": (987, 20000),
            "noise_margin": (18.8, 15.0),
            "attenuation": (24, 20)
        },

        "Bad" : {
            "payload_rate": (500, 2000),
            "actual_rate": (500, 2000),
            "attainable_rate": (600, 1024),
            "noise_margin": (0.9, 10),
            "attenuation": (25.1, 30)
        },

        "Down": {
            "payload_rate": (0, 0),
            "actual_rate": (0, 0),
            "attainable_rate": (0, 0),
            "noise_margin": (0, 0),
            "attenuation": (0, 0)
        },

        "NoSelt": {
            "payload_rate": (0, 0),
            "actual_rate": (0, 0),
            "attainable_rate": (0, 0),
            "noise_margin": (0, 0),
            "attenuation": (0, 0)
        }
    }

    def __init__(self, type):
        if not type in self.performance.keys():
            self.type = "Down"
        else:
            self.type = type

    def getLinePerformance(self, status=False):
            return self.performance[self.type] if status else self.performance["Down"]


## TEST CODE ##
if __name__ == '__main__':
    p = LinePerformance("Down")
    print(p.getLinePerformance())
