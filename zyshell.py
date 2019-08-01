import cmd
import sys
import tty
import termios
import re

class ZyShell(cmd.Cmd):
    prompt = 'ZyShell> '
    intro = """
ZyXEL IES6000 CLI Shell Simulator
Copyright(c) 2019 SHATEL, Customer Technical Support
Copyright(c) 2019 Reza Masoumvand <r.masoumvand@yahoo.com>
"""
    
    def getch(self):
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch
    
    
    def do_EOF(self, line):
        return True

    def default(self, line):
        print(line +": invalid command, valid commands are:")
        self.help(line)
    
    def help(self, line):
        print("""acl             alarm           clear           cluster
config          diagnostic      disable         enable
exit            ima             ip              ip6
lcman           multicast       port            profile
redundant       show            switch          sys
lan             voip
        """)

    def do_exit(self, line):
        return True

    def do_lc(self, line):
        if (line == "show"):
            print("""48V power: Input-A up, Input-B up
id state    card type          uptime f/w version         heat vol mon down out
-- -------- ----------- ------------- ------------------- ---------------------
 1 active   ALC1272G-51    6:12:06:51 V3.96(ARV.1)_0413     -   -   -    -   -
 2 active   ALC1272G-51    6:12:06:51 V3.96(ARV.1)_0413     -   -   -    -   -
 3 active   ALC1272G-51    6:12:06:50 V3.96(ARV.1)_0413     -   -   -    -   -
 4 active   ALC1272G-51    6:12:06:50 V3.96(ARV.1)_0413     -   -   -    -   -
 5 active   ALC1272G-51    6:12:06:51 V3.96(ARV.1)_0413     -   -   -    -   -
 6 active   ALC1272G-51    6:12:06:28 V3.96(ARV.1)_0413     -   V   -    -   -
 7 active   ALC1272G-51    6:12:06:27 V3.96(ARV.1)_0413     -   -   -    -   -
 8 active   MSC1024G       6:12:11:45 V4.05(AIN.0)          -   -   -    -   -
 9 -                                                        -   -   -    -   -
10 active   ALC1272G-51    6:12:06:49 V3.96(ARV.1)_0413     -   -   -    -   -
11 active   ALC1272G-51    6:12:06:27 V3.96(ARV.1)_0413     -   -   -    -   -
12 active   ALC1272G-51    6:12:06:30 V3.96(ARV.1)_0413     -   -   -    -   -
13 active   ALC1272G-51    6:12:06:51 V3.96(ARV.1)_0413     -   -   -    -   -
14 active   ALC1272G-51    6:12:06:49 V3.96(ARV.2)          -   -   -    -   -
15 active   ALC1272G-51    6:12:06:27 V3.96(ARV.1)_0413     -   -   -    -   -
16 active   ALC1272G-51    6:12:06:51 V3.96(ARV.1)_0413     -   -   -    -   -
17 active   ALC1272G-51    6:12:06:27 V3.96(ARV.1)_0413     -   -   -    -   -
""")

            
    def do_show(self, line):
        if (re.match("linestat \d+", line)):
            print("""                    usPayLoadRate dsPayLoadRate
port  link              (kbps)        (kbps)    protocol       up time
----- ------------- ------------- ------------- -------------- --------------
 1- 1 up                      639          4095 adsl2plus         6d12h 2m16s
 1- 2 up                     1039          2309 adsl2plus           19h13m59s
 1- 3 up                      866          3176 adsl2             6d12h 1m36s
 1- 4 up                     1017          1230 adsl2                3h30m22s
 1- 5 down                      0             0 none
 1- 6 up                      917         16382 adsl2plus         1d18h25m24s
 1- 7 up                     1032          2311 adsl2plus         6d12h 1m55s
 1- 8 down                      0             0 none
 1- 9 up                     1080         15848 adsl2plus            3h 1m
 1-10 up                      962          2309 adsl2plus         2d13h49m57s
 1-11 up                      705          5006 adsl2plus              35m10s
 1-12 up                      941          2309 adsl2plus         1d18h36m32s
 1-13 up                      767         10239 adsl2plus         1d21h25m 3s
 1-14 down                      0             0 none
 1-15 down                      0             0 none
 1-16 up                     1043         14025 adsl2plus         6d11h58m58s
 1-17 down                      0             0 none
 1-18 down                      0             0 none

                Press any key to continue, 'n' to nopause,'e' to exit""")
            ch=self.getch()
            if (ch == 'n'):
                print("""                usPayLoadRate dsPayLoadRate
port  link              (kbps)        (kbps)    protocol       up time
----- ------------- ------------- ------------- -------------- --------------
 1-19 down                      0             0 none
 1-20 down                      0             0 none
 1-21 down                      0             0 none
 1-22 up                      574          6140 adsl2plus           18h   18s
 1-23 down                      0             0 none
 1-24 up                     1062          9255 adsl2plus         6d12h 2m 5s
 1-25 down                      0             0 none
 1-26 up                      574          2271 adsl2plus           11h 7m22s
 1-27 up                      800          2144 gdmt                 5h53m22s
 1-28 up                     1009          2311 adsl2plus           20h40m23s
 1-29 down                      0             0 none
 1-30 down                      0             0 none
 1-31 up                      574          2271 adsl2plus            7h 3m 5s
 1-32 up                      767          4096 adsl2plus         5d22h 8m33s
 1-33 up                      639          2957 adsl2plus            1h32m 3s
 1-34 up                     1114          2306 adsl2plus         6d12h 2m14s
 1-35 down                      0             0 none
 1-36 up                     1148          2309 adsl2plus_m         21h 9m28s
 1-37 up                      574          4095 adsl2plus         1d    6m 2s
 1-38 up                      941          9256 adsl2plus           21h29m51s
 1-39 up                      727          1374 adsl2plus            2h36m21s
 1-40 up                      896          2304 t1413               21h46m15s
 1-41 up                     1032          9248 adsl2plus            2h40m45s
 1-42 down                      0             0 none
 1-43 down                      0             0 none
 1-44 down                      0             0 none
 1-45 down                      0             0 none
 1-46 down                      0             0 none
 1-47 down                      0             0 none
 1-48 up                     1151          7059 adsl2plus_m          9h11m31s
 1-49 down                      0             0 none
 1-50 up                     1141          9255 adsl2plus           23h35m
 1-51 up                      574          4095 adsl2plus         4d18h45m28s
 1-52 up                     1009          6070 adsl2plus         4d 9h59m44s
 1-53 down                      0             0 none
 1-54 up                     1151          5284 adsl2plus_m       4d13h32m40s
 1-55 down                      0             0 none
 1-56 up                      985          4862 adsl2plus            1h12m31s
 1-57 up                      574          2270 adsl2plus         6d12h 2m16s
 1-58 up                      958         16382 adsl2plus         6d12h 2m 6s
 1-59 up                     1130          9016 adsl2plus            1h 8m18s
 1-60 up                      747          5163 adsl2plus         6d11h14m47s
 1-61 down                      0             0 none
 1-62 up                      913          2492 adsl2plus         4d16h 9m50s
 1-63 down                      0             0 none
 1-64 down                      0             0 none
 1-65 up                     1047          2309 adsl2plus         2d 7h52m13s
 1-66 up                      574          2271 adsl2plus           18h   48s
 1-67 up                     1024          3184 adsl2plus            1h57m35s
 1-68 up                     1147          9249 adsl2plus         1d 9h 6m50s
 1-69 down                      0             0 none
 1-70 down                      0             0 none
 1-71 down                      0             0 none
 1-72 up                     1032          8072 adsl2plus               8m 3s""")
        elif (re.match("linerate \d+\-\d+", line)):
            print("""slot-port=1-72, DSL line rate
link                 = link_up
                       upstream   downstream
                       ---------- ----------
payload rate   (kbps)=       1032       8072
actual rate    (kbps)=       1041       8105
attainable rate(kbps)=       1119       8380
noise margin     (dB)=       10.7        8.6
attenuation      (dB)=       17.2       27.3""")
    def do_port(self, line):
        if (re.match("show \d+\-\d+", line)):
            print("""port 1-72
  name            :2611011127(davod hashemirad)
  telephone       :
  prof            :unlimited512
  alarm prof      :DEFVAL
  state           :enable
  mode            :auto
  pmm             :disable
  pmm l0time      :300 secs
  pmm l2time      :30 secs
  pmm l2atpr      :1 dB
  pmm l2atprt     :6 dB
  pmm l2minrate   :32 kbps
  pmm l2maxrate   :4096 kbps
  pmm l2threshold :16 kbps
  power adap.     :rate
  max us tx power :13.0 dBm
  max ds tx power :20.0 dBm
  max rx power    :0.0 dBm
  max us psd      :0.0 dBm/Hz
  max ds psd      :0.0 dBm/Hz

            Press any key to continue, 'e' to exit""")
            if (self.getch() != 'e'):
                print("""  annexl          :disable
  annexm          :disable
  annexi          :disable
  us_inpmin       :0.5 DMT symbols
  ds_inpmin       :0.5 DMT symbols
  option_mask     :0x0000
  uscarrier       :
   31~0      63~32
  00000000  00000000
  dscarrier       :
             63~32     95~64    127~96    159~128   191~160   223~192   255~224
            00000000  00000000  00000000  00000000  00000000  00000000  00000000

  287~256   319~288   351~320   383~352   415~384   447~416   479~448   511~480
  00000000  00000000  00000000  00000000  00000000  00000000  00000000  00000000

            Press any key to continue, 'e' to exit""")
                if (self.getch() != 'e'):
                    print("""pvc setting:
pvc              type    mux   pvid  pri  profile
--------------- ------- ----- ------ ---- --------------------------------
1-72-0/35       pvc      llc     213    0 DEFVAL

            Press any key to continue, 'e' to exit
vlan setting:
 vid  port/pvc         type     adv     untag
----- --------------- ------- -------- --------
  213 1-72-0/35       pvc          fix    untag""")


    def do_diagnostic(self, line):
        if (re.match("selt show \d+\-\d+", line)):
            print(""" port     inprogress       cableType loopEstimateLength
----- -------------------- --------- ------------------
 1-19                 DONE     24AWG    2275 m(7.46 kFt)""")
                    
if __name__ == '__main__':
    ZyShell().cmdloop()
