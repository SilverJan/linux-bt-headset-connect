#!/usr/bin/env python3

import logging
import yaml

def getLogger():
    logger = logging.getLogger("btctl")
    logger.setLevel(logging.DEBUG)

    # Enable logging to console
    if len(logger.handlers) < 1:
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
        logger.addHandler(ch)

    return logger

def getHeadsetDetails():
    with open("config.yaml") as config:
        try: # Python >= 3.7
            headset_details = yaml.load(config, Loader=yaml.FullLoader)
        except: # Python < 3.7
            headset_details = yaml.load(config)
    return headset_details

def replaceColonWithUnderline(str):
    return str.replace(':', '_')
