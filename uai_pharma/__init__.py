import os
from pip._internal.utils import logging

newDict = {}
logger = logging.getLogger(__name__)
env_name = '.env'

try:
    f = open(env_name, 'r')
    for line in f:
        listedline = line.strip().split('=')
        if len(listedline) > 1:
            newDict[listedline[0]] = listedline[1]
except FileNotFoundError:
    logger.error("Falha na abertura do arquivo " + env_name)
finally:
    os.environ.update(newDict)