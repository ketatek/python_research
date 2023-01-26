#!/usr/bin/env python

import sys
from logging import(
    getLogger
    , StreamHandler
    , Formatter
    , INFO
)

import json, logging.config

def create_logger_001():

    logger = getLogger(__name__)
    logger.setLevel(INFO)

    formatter = Formatter(  
        '%(created)f:%(levelname)s:%(name)s:%(module)s:%(message)s'
    )

    handler = StreamHandler(sys.stderr)
    handler.setLevel(INFO)
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)

    return logger

def create_logger_001():

    with open('log-config.json', 'rt') as f:
        config = json.load(f)
        logging.config.dictConfig(config)
    
    logger = getLogger(__name__)

    return logger
