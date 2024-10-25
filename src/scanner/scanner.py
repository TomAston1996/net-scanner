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

from typing import TypedDict

from src.logger import Log
from src.scanner.iscan import IScan

class PortInfo(TypedDict):
    port: str
    port_name: str
    port_state: str

class HostInfo(TypedDict):
    host_name: str
    host_os: str
    host_state: str
    protocol: str
    ports: list[PortInfo]

class Scanner(IScan):
    '''
    Brief: network port scannner
    '''
    log = Log.get_instance()

    __host_info_template: HostInfo = {
        'host_name': '',
        'host_os': '',
        'host_state': '',
        'protocol': '',
        'ports': [],
    }

    __port_info_template: PortInfo = {
        'port': '',
        'port_name': '',
        'port_state': '',
    }

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
        self._get_host_info()


    def _get_host_info(self) -> list[HostInfo]:
        '''
        Brief: find all available hosts on the network
        '''
        hosts_info = []
        
        for host in self.nm.all_hosts():
            host_info = self.__host_info_template.copy()
            
            host_name = self.nm[host].hostname()
            os_match = self.nm[host]["osmatch"]
            host_os = os_match[0]["name"] if len(os_match) > 0 else "No Match"
            host_state = self.nm[host].state()

            host_info['host_name'] = host_name
            host_info['host_os'] = host_os
            host_info['host_state'] = host_state

            print('----------------------------------------------------')
            print(f'Host : {host} ({host_name})')
            print(f'Host OS: {host_os}')
            print(f'State : {host_state}')
            for proto in self.nm[host].all_protocols():
                print('----------')
                print(f'Protocol : {proto}')
                host_info['protocol'] = proto

                lport = self.nm[host][proto].keys()
                for port in lport:
                    port_info = self.__port_info_template.copy()
                    
                    port_state = self.nm[host][proto][port]['state']
                    port_name = self.nm[host][proto][port]['name']

                    port_info['port'] = port
                    port_info['port_name'] = port_name
                    port_info['port_state'] = port_state

                    host_info['ports'].append(port_info)
                    
                    print(f'port : {port} ({port_name})\tstate : {port_state}')

            hosts_info.append(hosts_info)

            print('\n')
        
        self.log.log_info("Port & OS scan complete", "scanner.py")

        return hosts_info


            