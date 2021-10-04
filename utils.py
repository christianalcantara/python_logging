from logger import _logger


def stdout(string):
    _logger.info("Print: {}".format(string))
    print(string)
