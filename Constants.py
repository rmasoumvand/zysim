LINE_STAT_HEADER = """
                    usPayLoadRate dsPayLoadRate
port  link              (kbps)        (kbps)    protocol      up time
----- ------------- ------------- ------------- ------------- -------------"""

LINE_STAT_INFO = "{:<2d}-{:<2d} {:<4s}                   {:<5d}        {:<5d} {:<9s}     {:<12s}"

DIAG_SELT_RESULT = """
 port     inprogress       cableType loopEstimateLength
----- -------------------- --------- ------------------
 {}-{}           {}     {}    {}"""

DIAG_SELT_METER = "{:>4s} m({:1.2f} kFt)"


LINE_RATE = """
slot-port={}-{}, DSL line rate
link                 = link_{}
                       upstream   downstream
                       ---------- ----------
payload rate   (kbps)=        {}      {}
actual rate    (kbps)=        {}      {}
attainable rate(kbps)=        {}      {}
noise margin     (dB)=        {}      {}
attenuation      (dB)=        {}      {}
"""

HELP = """
acl             alarm           clear           cluster
config          diagnostic      disable         enable
exit            ima             ip              ip6
lcman           multicast       port            profile
redundant       show            switch          sys
vlan            voip
"""

ADSL2PLUS = "adsl2plus"

STATUS_UP = "up"
STATUS_DOWN = "down"



if __name__ == '__main__':
    print(DIAG_SELT_RESULT.format(1,2,"INPROGRESS","24AWG", DIAG_SELT_METER.format(5000,12.65)))
    print()
    print(HELP)
