#  _   _      _    _____                                 
# | \ | |    | |  / ____|                                
# |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
# | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
# |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_| 
 
from src.logger import Log
from src.scan.scanner import Scanner

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
    scanner.set_ip_range('192.168.1.1/24')
    # scanner.set_ip_range('192.168.1.254')
    
    scanner.scan()
    scanner.get_host_info()