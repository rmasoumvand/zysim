#!/usr/bin/env python3

from DSLAM import DSLAM
import sys
import tty
import termios
import re
import Constants


def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    tty.setraw(fd)
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch


print("""ZySIM (ZyXEL IES6000 CLI Simulator
Copyright(c) 2018 SHATEL, Department of Customer Technical Support
Copyright(c) 2018 Reza Masoumvand <r.masoumvand@yahoo.com>
""")

dslam = DSLAM(10)

reg_linerate = re.compile("show\slinerate\s[0-9]{1,2}-[0-9]{1,2}")
reg_linestat = re.compile("show\slinestat\s[0-9]{1,2}-[0-9]{1,2}")
reg_linestat_all = re.compile("show\slinestat\s[0-9]{1,2}")
reg_diag_selt_test = re.compile("diagnostic\sselt\stest\s[0-9]{1,2}-[0-9]{1,2}")
reg_diag_selt_show = re.compile("diagnostic\sselt\sshow\s[0-9]{1,2}-[0-9]{1,2}")

try:

    while True:
        cmd = str(input("ZySim> "))

        if cmd == 'exit':
            break
        elif cmd == 'help' or cmd == '?':
            print(Constants.HELP)
        elif cmd == '':
            pass
        elif '-' in cmd:
            cmd_arr = cmd.split(' ')
            
            if len(cmd_arr) == 3:
                slot, port = (cmd_arr[2].split('-'))
                
            elif len(cmd_arr) == 4:
                slot, port = (cmd_arr[3].split('-'))
            
            if re.match(reg_linerate, cmd):
                #Exec Linerate
                print(dslam.getSlot(int(slot)).getLinerate(int(port)))
                
            elif re.match(reg_linestat, cmd):
                #Exec Linestat
                print(dslam.getSlot(int(slot)).getLineStat(int(port)))

            elif re.match(reg_diag_selt_test, cmd):
                dslam.getSlot(int(slot)).getDiagSeltTest(int(port))
                
            elif re.match(reg_diag_selt_show, cmd):
                #Exec Diagnostic Selt Show
                print(dslam.getSlot(int(slot)).getDiagSeltShow(int(port)))
                
        elif re.match(reg_linestat_all, cmd):
                slot = (cmd.split(' ')[-1])
                print(Constants.LINE_STAT_HEADER)
                non_pause = False
                for i in range(1, 73):
                    print(dslam.getSlot(int(slot)).getLineStat(i))
                    if (i%18 == 0) and not non_pause:
                        print("\r\n\tPress any key to continue, 'n' to nopause,'e' to exit")
                        ch = getch()
                        if (ch == 'e'):
                            break
                        elif (ch == 'n'):
                            non_pause = True
                            continue
                        else:
                            continue
                
        else:
            print("\r\nInvalid command, valid commands are: {}".format(Constants.HELP))
except KeyboardInterrupt:
    print("\n\nBye, bye...")
except EOFError:
    print("\n\nBye, bye...")

