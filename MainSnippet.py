#!/usr/bin/env/python

""" MailSender.py : Python script to demonstrate use of emails """

__author__ = "Mohit Kumar"
__credits__ = ["Mohit Kumar"]
__version__ = "1.0.0"
__maintainer__ = "Mohit Kumar"
__email__ = "mohitkumar2801@gmail.com"
__status__ = "Production"

# Todo :
# 1. Logging DONE
# 2. Read Configuration ( Yaml )
# 3. SQL DB Connection
# 4. File Interface
# 5. Command line argument reading

import os
import sys
import logging
import argparse
from datetime import datetime

import yaml

JOB_NAME = 'MainSnippet'

CONFIG_FILE_NAME = 'config.yaml'
INPUT_DIR_NAME = 'input'
OUTPUT_DIR_NAME = 'output'
LOG_DIR_NAME = 'logs'

LOGGING_LOG_FORMAT = "%(asctime)s [ %(levelname)s ] : %(message)s"
LOGGING_DATE_FORMAT = "%Y%m%d %H:%M:%S"
LOGGING_LEVEL = logging.DEBUG

CLI_ARGS = None
LOGGER = None

def assign_logging_from_config( logging_text ):
    """ Method to assign logging level from configurations """
    logging_values = {
        "DEBUG" : logging.DEBUG,
        "INFO" : logging.INFO,
        "WARN" : logging.WARN,
        "ERROR" : logging.ERROR,
        "CRITICAL" : logging.CRITICAL
    }
    return logging_values.get( logging_text, logging.DEBUG )

def init_configurations():
    """ Method to load configurations from primary config file """
    print( "Initialized configuration file reading." )

    global CONFIG_FILE_NAME
    global LOGGING_LEVEL

    if CLI_ARGS.config:
        CONFIG_FILE_NAME = CLI_ARGS.config
    
    print( "Reading from %s"%( CONFIG_FILE_NAME ) )

    if not os.path.exists( CONFIG_FILE_NAME ):
        print( "Configuration file not found! Exiting." )
        sys.exit( os.EX_NOINPUT )

    with open( CONFIG_FILE_NAME ) as config_file_obj:
        configuration = yaml.load( config_file_obj, Loader=yaml.FullLoader )

        LOGGING_LEVEL = assign_logging_from_config( configuration['logging'] )

def generate_log_file_name():
    return "".join( [ JOB_NAME, '_', datetime.now().strftime('%Y%m%d%H%M%S'), '.log' ] )

def init_logging():
    """ Method to initialize logging configurations """
    print( "Initialized file logging." )

    global LOGGER

    LOGGER = logging.getLogger( "Logger" )
    LOGGER.setLevel( LOGGING_LEVEL )

    formatter = logging.Formatter( LOGGING_LOG_FORMAT, LOGGING_DATE_FORMAT )

    fileHandler = logging.FileHandler( os.path.join( LOG_DIR_NAME, generate_log_file_name() ) )
    fileHandler.setLevel( LOGGING_LEVEL )
    fileHandler.setFormatter( formatter )

    streamHandler = logging.StreamHandler()
    streamHandler.setLevel( LOGGING_LEVEL )
    streamHandler.setFormatter( formatter )

    LOGGER.addHandler( fileHandler )
    LOGGER.addHandler( streamHandler )

def init_argument_parsing():
    """ Method to initialize command line argument configurations """
    print( "Initialized command line argument parsing." )
    global CLI_ARGS
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument( "-c", "--config", help="To provide runtime configuration file" )
    CLI_ARGS = argument_parser.parse_args()

def init_directories():
    """ Method to initialize work directories if not exists """
    print( "Initialized Directory creation. Creating directories if not exist." )
    if not os.path.exists( INPUT_DIR_NAME ):
        os.mkdir( INPUT_DIR_NAME )
    if not os.path.exists( OUTPUT_DIR_NAME ):
        os.mkdir( OUTPUT_DIR_NAME )
    if not os.path.exists( LOG_DIR_NAME ):
        os.mkdir( LOG_DIR_NAME )

def init_db_connection():
    """ Method to initialize MySQL DB Connection if not exists """
    pass

def initialize():
    """ Initializer method : To initialize objects """
    init_directories()
    init_argument_parsing()
    init_configurations()
    init_logging()
    LOGGER.info( f"Initialization finished for Job : {JOB_NAME}" )

def execute():
    """ Execute method : To contain the main logic """
    LOGGER.debug( "Entering execute method." )
    LOGGER.debug( "Exiting execute method." )

def finalize():
    """ Finalizer method : To gracefully close connections """
    LOGGER.debug( "Entering finalizer method." )
    LOGGER.debug( "Exiting finalizer method." )

if __name__ == "__main__":

    initialize()

    execute()

    finalize()