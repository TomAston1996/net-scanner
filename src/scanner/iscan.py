#  _   _      _    _____                                 
# | \ | |    | |  / ____|                                
# |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
# | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
# |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_| 
'''
File: iscan.py
Brief: scanner interface
Author: Tom Aston
'''

from abc import ABCMeta, abstractmethod
from typing import TypedDict


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


class IScan(metaclass=ABCMeta):
    '''
    Brief:     interface for scanner class
    '''

    @abstractmethod
    def scan(self) -> None:
        '''
        Brief: scan
        '''

    @abstractmethod
    def get_host_info(self) -> list[HostInfo]:
        '''
        Brief: returns a list of host info from the
        '''