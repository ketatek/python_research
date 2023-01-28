#!/usr/bin/env python

import sys
from logging import(
    getLogger
    , StreamHandler
    , Formatter
    , INFO, DEBUG
)

import json, logging.config

def create_logger_001():

    logger = getLogger(f"{__name__}_001")
    logger.setLevel(INFO)

    formatter = Formatter(  
        fmt='%(asctime)s > [%(levelname)s] %(module)s > %(message)s'
    )

    handler = StreamHandler(sys.stderr)
    handler.setLevel(DEBUG)
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)

    return logger

def create_logger_002():

    with open('logging.json', 'rt') as f:
        config = json.load(f)
        logging.config.dictConfig(config)
    
    logger = getLogger(f"{__name__}_002")

    return logger

