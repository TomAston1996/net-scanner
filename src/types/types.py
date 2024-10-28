#  _   _      _    _____                                 
# | \ | |    | |  / ____|                                
# |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
# | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
# |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_| 
'''
File: types.py
Brief: contains all custom types used in net-scanner
Author: Tom Aston
'''
from typing import TypedDict

class PortInfo(TypedDict):
    port: str
    port_name: str
    port_state: str
    port_cpe: str
    port_version: str


class HostInfo(TypedDict):
    host_name: str
    host_os: str
    host_state: str
    protocol: str
    ports: list[PortInfo]