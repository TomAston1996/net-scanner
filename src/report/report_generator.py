#  _   _      _    _____                                 
# | \ | |    | |  / ____|                                
# |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
# | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
# |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_| 
'''
File: report_generator.py
Brief: output excel report based on active hosts and their vulnerabilities
Author: Tom Aston
'''
import os
import pandas as pd

from src.logger import Log
from src.report.ireport_generator import IReportGenerator
from src.types.types import HostInfo

class ReportGenerator(IReportGenerator):
    '''
    Brief: report generation for host and vulnerability scans
    '''
    log = Log.get_instance()

    def __init__(self) -> None:
        pass

    def generate_host_report(self, data: list[HostInfo]) -> None:
        '''
        Breif: output active host report to pwd
        '''
        cwd = os.getcwd()

        hosts_dataframe = self.transform_host_data(data)
        hosts_dataframe.to_csv(f'{cwd}\\hosts.csv')

        self.log.log_info(f'Host report saved at {cwd}', self.__class__.__name__)

    def transform_host_data(self, data: list[HostInfo]) -> pd.DataFrame:
        '''
        Breif: create df and transform host data to be exported as csv
        '''
        hosts_dataframe = pd.DataFrame(data)
        hosts_dataframe = hosts_dataframe.explode(['ports']).reset_index(drop=True)
        ports_dataframe = pd.json_normalize(hosts_dataframe['ports']).reset_index(drop=True)

        df_merged = pd.concat([hosts_dataframe, ports_dataframe], axis=1).drop(['ports'], axis=1)

        return df_merged
