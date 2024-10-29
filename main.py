#  _   _      _    _____                                 
# | \ | |    | |  / ____|                                
# |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
# | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
# |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_| 
'''
File: main.py
Brief: application entry point
Author: Tom Aston
'''
from src.logger import Log
from src.scan.scanner import Scanner
from src.exploit.vuln_searcher import VulnSearcher
from src.report.report_generator import ReportGenerator

if __name__ == "__main__":

    # user interface header
    print(r"""
     _   _      _    _____                                 
    | \ | |    | |  / ____|                                
    |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
    | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
    | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
    |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_|
    """)
    print("\n****************************************************************")
    print("\n* Copyright of Tom Aston, 2024                              *")
    print("\n* https://www.tomaston.dev                                  *")
    print("\n****************************************************************")
    
    logger = Log.get_instance() # singleton

    while True:
        report_generator = ReportGenerator()
        scanner = Scanner()

        #for windows use ipconfig to obtain IPv4 LAN addresses & subnet mask to find range
        # scanner.set_ip_range('192.168.1.1/24')
        scanner.set_ip_range('192.168.1.144')

        vuln_searcher = VulnSearcher(scanner, report_generator)

        has_host_scanned = False
        while (not has_host_scanned):
            host_scan_response = input(f'Start host scan? (y/n): ').lower()
            if (host_scan_response == 'y'):
                vuln_searcher.scan_hosts()
                vuln_searcher.output_host_report()
                has_host_scanned = True
        

        vuln_scan_response = input('Conduct vulnerability scan? (y/n): ').lower()
        if (vuln_scan_response == 'y'):
            vuln_searcher.search_vulnerability_on_cpe_criteria()
        
        #TODO implement reset method in Scanner and VulnSearcher
        is_reset = input('Reset? (y/n): ').lower()
        if (is_reset == 'n'): break
