#  _   _      _    _____                                 
# | \ | |    | |  / ____|                                
# |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
# | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
# |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_| 
'''
File: ireport_generator.py
Brief: interface for ReportGenerator class
Author: Tom Aston
'''

from abc import ABCMeta, abstractmethod
from typing import TypedDict

class IReportGenerator(metaclass=ABCMeta):
    '''
    Brief:     interface for ReportGenerator class
    '''

    @abstractmethod
    def out(self) -> None:
        '''
        Brief: output report
        '''