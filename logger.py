import logging
import sys


def _init_logger():
    logger = logging.getLogger('app')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('std.log')
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(created)f:%(levelname)s:%(name)s:%(module) s:%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


_init_logger()
_logger = logging.getLogger('app')
