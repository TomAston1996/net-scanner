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
from yaspin import yaspin

from src.logger import Log
from src.scan.iscanner import IScanner
from src.types.types import HostInfo
from src.types.types import PortInfo

class Scanner(IScanner):
    '''
    Brief: network port scannner
    '''
    log = Log.get_instance()

    __host_info_template: HostInfo = {
        'host_ip': '',
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

    IP_RANGE: str = ''

    def __init__(self) -> None:
        '''
        Brief: scanner contructor method
        '''
        self.nm = nmap.PortScanner()

    def set_ip_range(self, ip_range: str) -> None:
        '''
        Brief: set ip range to be scanned - can be an IP address or range
        '''
        self.IP_RANGE = ip_range

    def _scan_ip_range(self) -> None:
        '''
        Brief: scan ip range as part of object initialisation

        -sS performs a TCP SYN port scan. This type of scan is relatively quick but also stealthy as it only completes half handshake
        -O enables OS detection
        -sV enables version detection
        '''
        self.log.log_info('Scanning all IPs within range. This can take a while...', self.__class__.__name__)
        self.nm.scan(hosts=self.IP_RANGE, arguments='-sS -O -sV')
        self.log.log_info('Network scan complete', self.__class__.__name__)

    def get_host_info(self) -> list[HostInfo]:
        '''
        Brief: find all available hosts on the network

        CPE=Common Platform Enumeration
        i.e. cpe:/o:linux:linux_kernel where cpe:/o:{vendor}:{product}
        '''
        self._scan_ip_range()

        hosts_info = []
        
        for host in self.nm.all_hosts():
            host_info = self.__host_info_template.copy()
            
            host_name = self.nm[host].hostname()
            os_match = self.nm[host]["osmatch"]
            host_os = os_match[0]["name"] if len(os_match) > 0 else "No Match"
            host_state = self.nm[host].state()

            host_info['host_ip'] = host
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
                    port_cpe = self.nm[host][proto][port]['cpe']
                    port_version = self.nm[host][proto][port]['version']

                    # self.to_json(self.nm[host])

                    port_info['port'] = port
                    port_info['port_name'] = port_name
                    port_info['port_state'] = port_state
                    port_info['port_cpe'] = port_cpe
                    port_info['port_version'] = port_version

                    host_info['ports'].append(port_info)
                    
                    print(f'port : {port} ({port_name})\tstate : {port_state}\tcpe : {port_cpe}\tversion : {port_version}')

            hosts_info.append(host_info)

            print('\n')
        
        self.log.log_info("Port & OS scan complete", self.__class__.__name__)

        self.to_json(host_info, 'test')

        return hosts_info
    
    def to_json(self, dict: dict, file_name: str) -> None:
        '''
        Brief: dictionary to json
        '''
        with open(f'./local/{file_name}.json', "w") as outfile: 
            json.dump(dict, outfile)
