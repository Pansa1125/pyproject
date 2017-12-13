# -*- coding = utf-8 -*-
import logging
import string
import logging.config
def use_logger(user, loglevel):
    logging.config.fileConfig('logconfig')
    logger = logging.getLogger('root')
    log_demo = loglevel.strip()
    if log_demo == 'debug':
        logger.debug()
    elif log_demo == 'info':
        logger.info()
    elif log_demo == 'warn':
        logger.warn()
    else:
        logger.error()
