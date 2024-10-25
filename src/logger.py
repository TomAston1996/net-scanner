#  _   _      _    _____                                 
# | \ | |    | |  / ____|                                
# |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
# | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
# |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_| 

'''
File: logger.py
Brief: JSON Logger for NetScanner
Author: Tom Aston
'''
import json
import datetime
import os


class Log(object):
    '''
    Brief: JSON class for logger
    Logs JSON messages and displays them
    '''
    __logger_template = {
        'Error number': '',
        'Error message': '',
        'Error location': '',
        'Error Object': '',
        'Additional data': '',
        'Time': '',
        'Version number': '',
    }

    __logger_info_template = {
        'Info': '',
        'Info Location': '',
        'Time': '',
        'Version number': ''
    }

    _instance = None

    _filepath = f"{os.getenv('APPDATA')}/NetScanner/"
    _filename = r"NetScannerLog.json"

    _main_view = None

    def __new__(cls):
        if cls._instance is None:
            print('Logger Singleton Init')
            cls._instance = super(Log, cls).__new__(cls)
        return cls._instance

    def __check_dir_exists(self) -> None:
        print(f"Checking dir -  {self._filepath}")
        if not os.path.exists(self._filepath):
            print("mkdir NetScanner")
            os.mkdir(self._filepath)

    def log_error(self, error_number: int, error_message: str, error_location: str, error_object: Exception,  additional_data: str) -> None:
        '''
        Brief: Writes a JSON log for a particular error
        '''
        logger_print = self.__logger_template.copy()

        logger_print['Error number'] = error_number
        logger_print['Error message'] = error_message
        logger_print['Error location'] = error_location
        logger_print['Error Object'] = str(error_object)
        logger_print['Additional data'] = additional_data
        logger_print['Time'] = str(datetime.datetime.now())
        logger_print['Version number'] = '1.0'
        
        print("[{}][Error] {}: {}".format( logger_print['Time'], error_number, error_message))
        
        self.__logger_file_print(logger_print)

    def log_info(self, info_message: str, info_location: str) -> None:
        '''
        Brief: Log info rather than an error
        '''
        logger_print = self.__logger_info_template.copy()

        logger_print['Info'] = info_message
        logger_print['Info Location'] = info_location
        logger_print['Time'] = str(datetime.datetime.now())
        logger_print['Version number'] = '1.0'
        
        print("[{}][INFO] {}: {}".format( logger_print['Time'], info_location, info_message))
        self.__logger_file_print(logger_print)

    def __logger_file_print(self, logger_json: dict):
        self.__check_dir_exists()
        with open(self._filepath + self._filename, 'a', encoding='utf-8') as file:
            file.write(json.dumps(logger_json, indent=4)+',\n')
