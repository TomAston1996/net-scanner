#  _   _      _    _____                                 
# | \ | |    | |  / ____|                                
# |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
# | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
# |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_| 
'''
File: scanner.py
Brief: scanner class
Author: Tom Aston
'''

import nmap
import ipaddress
import re

from src.logger import Log
from src.scanner.iscan import IScan

class Scanner(IScan):
    '''
    Brief: network port scannner
    '''

    log = Log()

    def __init__(self) -> None:
        '''
        Brief: scanner contructor method
        '''
        self.nm = nmap.PortScanner()
        self._scan_ip_range()

    def _scan_ip_range(self) -> None:
        '''
        Brief: scan ip range as part of object initialisation

        -sS performs a TCP SYN port scan. This type of scan is relatively quick but also stealthy as it only completes half handshake
        -O enables OS detection
        '''
        self.nm.scan(hosts='192.168.1.1/24', arguments='-sS -O')

    def scan(self, ) -> None:
        '''
        Brief: entry method
        '''
        self._get_all_hosts()

    def _get_all_hosts(self) -> list[str]:
        '''
        Brief: find all available hosts on the network
        '''
        self.log.log_info('finding all hosts...', 'scanner.py')

        for host in self.nm.all_hosts():
            print('----------------------------------------------------')
            print(f'Host : {host} ({self.nm[host].hostname()})')
            print(f'State : {self.nm[host].state()}')
            for proto in self.nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)

                lport = self.nm[host][proto].keys()
                for port in lport:
                    print ('port : %s\tstate : %s' % (port, self.nm[host][proto][port]['state']))
            
