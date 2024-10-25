#  _   _      _    _____                                 
# | \ | |    | |  / ____|                                
# |  \| | ___| |_| (___   ___ __ _ _ __  _ __   ___ _ __ 
# | . ` |/ _ \ __|\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
# | |\  |  __/ |_ ____) | (_| (_| | | | | | | |  __/ |   
# |_| \_|\___|\__|_____/ \___\__,_|_| |_|_| |_|\___|_| 

from src.logger import Log

if __name__ == "__main__":
    #set up Logger singleton instance
    logger = Log()

    logger.log_info("Logger singleton initialised", "main.py")
    logger.log_error(1, "Error123", "main.py", ValueError, "some additional data...")