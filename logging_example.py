import logging
logging.basicConfig(level=logging.DEBUG)

def without_logger():
    for i in range(1,101):
        print(i)
    return "Task complete"
def with_logging():
    logger = logging.getLogger('Print 1 to 100 application')

    for i in range(1,101):
        logger.debug("Printing in Debug mode(Level 10) : {}".format(i))
        logger.info("Printing in Info mode(Level 20) : {}".format(i))
        logger.warning("Printing in Warning mode(Level 30) : {}".format(i))
        logger.error("Printing in Error mode(Level 40) : {}".format(i))
        logger.critical("Printing in Critical mode(Level 50) : {}".format(i))

if __name__ == '__main__':
    #without_logger()
    with_logging()