"""
Capture program flow and errors using Python's built-in logging module
"""

import logging

def setup_logging():

    """
    Sets up a logger with seperate file and stream handlers. 
    It will log DEBUG and up to a seperate file and INFO and up to the console

    RETURNS:
        logging.logger: configures logger instance
    """
    logger = logging.getLogger("currency_converter")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers: #Prevents duplicates handlers

        # File handler will log everything
        fh = logging.FileHandler("converter.log")
        fh.setLevel(logging.DEBUG)

        #stream handler will show info and up.
        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        
        #formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(sh)

    return logger
