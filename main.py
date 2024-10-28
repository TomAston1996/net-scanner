#  _   _      _    _____                                 
# | \ | |    | |  / ____|                                
# |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
# | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
# |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_| 
 
from src.logger import Log
from src.scan.scanner import Scanner
from src.exploit.vuln_searcher import VulnSearcher

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

    scanner = Scanner()

    #for windows use ipconfig to obtain IPv4 LAN addresses & subnet mask to find range
    # scanner.set_ip_range('192.168.1.1/24')
    scanner.set_ip_range('192.168.1.144')

    vuln_searcher = VulnSearcher(scanner, None)

    has_host_scanned = False
    while (not has_host_scanned):
        print('Start host scan? (y/n): ')
        host_scan_response = str(input()).lower()
        if (host_scan_response == 'y'): 
            vuln_searcher.scan_hosts()
            has_host_scanned = True
    

    print('Conduct vulnerability scan? (y/n): ')
    vuln_scan_response = str(input()).lower()
    if (vuln_scan_response == 'y'):
        vuln_searcher.search_vulnerability_on_cpe_criteria()
    
    #TODO implement reset method in Scanner and VulnSearcher
    print('Reset? (y/n): ')
