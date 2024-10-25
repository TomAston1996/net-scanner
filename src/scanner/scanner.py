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
import json
import ipaddress
import re

from src.logger import Log
from src.scanner.iscan import IScan

class Scanner(IScan):
    '''
    Brief: network port scannner
    '''
    log = Log.get_instance()

    def __init__(self) -> None:
        '''
        Brief: scanner contructor method
        '''
        self.nm = nmap.PortScanner()


    def _scan_ip_range(self, ip_range: str) -> None:
        '''
        Brief: scan ip range as part of object initialisation

        -sS performs a TCP SYN port scan. This type of scan is relatively quick but also stealthy as it only completes half handshake
        -O enables OS detection
        '''
        self.log.log_info('Scanning all IPs within range. This can take a while...', 'scanner.py')
        self.nm.scan(hosts=ip_range, arguments='-sS -O')
        self.log.log_info('Network scan complete', 'scanner.py')


    def scan(self, ip_range: str) -> None:
        '''
        Brief: entry method
        '''
        self._scan_ip_range(ip_range)
        self._get_all_hosts()


    def _get_all_hosts(self) -> list[str]:
        '''
        Brief: find all available hosts on the network
        '''
        for host in self.nm.all_hosts():
            os_match = self.nm[host]["osmatch"]
            print('----------------------------------------------------')
            print(f'Host : {host} ({self.nm[host].hostname()})')
            print(f'Host OS: {os_match[0]["name"] if len(os_match) > 0 else "No Match"}')
            print(f'State : {self.nm[host].state()}')
            for proto in self.nm[host].all_protocols():
                print('----------')
                print(f'Protocol : {proto}')

                lport = self.nm[host][proto].keys()
                for port in lport:
                    state = self.nm[host][proto][port]['state']
                    print(f'port : {port}\tstate : {state}')
            print('\n')
        
        self.log.log_info("Port & OS scan complete", "scanner.py")

        return []


            