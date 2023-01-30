#!/usr/bin/env python
#!/usr/bin/env python

import sys
from logging import(
    getLogger
    , StreamHandler
    , FileHandler
    , Formatter
    , INFO, DEBUG,
)

import json, logging.config


def create_logger_101():

    logger = getLogger(f"{__name__}_101")
    logger.setLevel(DEBUG)

    formatter = Formatter(  
        fmt='%(asctime)s > [%(levelname)s] %(module)s > %(message)s'
    )

    h01 = StreamHandler(sys.stderr)
    h01.setLevel(INFO)
    h01.setFormatter(formatter)
    

    h02 = FileHandler("rlog_02_101.log")
    h02.setLevel(DEBUG)
    h02.setFormatter(formatter)

    logger.addHandler(h01)
    logger.addHandler(h02)

    return logger


def create_logger_102():

    logger = getLogger(f"{__name__}_101")
    logger.setLevel(DEBUG)

    formatter = Formatter(  
        fmt='%(asctime)s > [%(levelname)s] %(module)s > %(message)s'
    )

    h01 = StreamHandler(sys.stderr)
    h01.setLevel(INFO)
    h01.setFormatter(formatter)
    

    h02 = FileHandler("rlog_02_101.log")
    h02.setLevel(DEBUG)
    h02.setFormatter(formatter)

    logger.addHandler(h01)
    logger.addHandler(h02)

    return logger
