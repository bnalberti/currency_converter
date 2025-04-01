"""
Capture program flow and errors using Python's built-in logging module
"""

import logging

def setup_logging():
    logger = logging.getLogger("currency_converter")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler("converter.log")
        sh = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(sh)

    return logger
