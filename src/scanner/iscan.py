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

class IScan(metaclass=ABCMeta):
    '''
    Brief:     interface for scanner class
    '''

    @abstractmethod
    def scan(self) -> None:
        '''
        Brief: scan
        '''