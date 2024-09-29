import logging
import os

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not os.path.exists('./log'):
        os.makedirs('./log')
    formatter = logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename="./log/log.log")
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

logger = get_logger(__name__)