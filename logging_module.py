'''
 datefmt='%m/%d/%Y %I:%M:%S %p'
'''
import logging
import time

logging.basicConfig(level=logging.ERROR,
                    format='%(levelname)s %(name)-2s %(asctime)-2s %(message)s',
                    datefmt='%m-%d::%Y %H:%M',
                    filename='debug.log',
                    filemode='w')

logging.info(' :: INFO')
logging.debug(' :: debug info')
logging.warning(' :: Warning is')
logging.error(' :: Error info')
logging.critical(" :: critical info")