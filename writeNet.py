#!/usr/bin/env python2.7

""" Writes network information to LCD.

"""

__author__ = 'Igor Janjic'
__version__ = '0.1'


import pmod
import socket
import time
import sys


def main():
    time.sleep(60)
    try:
        baudRate = 9600
        accessType = pmod.AccessType.UART
        p = pmod.PMOD(accessType, baudRate)
        while True:
            time.sleep(5)
            p.dispClear()
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 0))
            host = socket.gethostname()
            addr = s.getsockname()[0]
            p.write(host, 0, 0)
            p.write(addr, 1, 0)
    except socket.error:
            pass
    except pmod.ErrorWrite as e:
        print(e.msg)
    except pmod.ErrorPMOD as e:
        print(e.msg)
    except KeyboardInterrupt:
        print('\nClosing.')
        sys.exit(0)

if __name__ == '__main__':
    main()
