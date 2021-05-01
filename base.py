""" 

base.py :

Generated with Automatron

"""

__author__ = "Mohit Kumar"
__credits__ = ["Mohit Kumar"]
__version__ = "1.0.0"
__maintainer__ = "Mohit Kumar"
__email__ = "mohitkumar2801@gmail.com"
__status__ = "Production"


import os
import sys
import threading
import logging
from datetime import datetime

import pyfiglet

PROCESSOR_THREADS = 8

LOGS_DIR = 'logs'
INPUT_DIR = 'input'
OUTPUT_DIR = 'output'


logging.basicConfig(level=logging.DEBUG)

#################################################################################
# Private Methods ###############################################################
#################################################################################

def _print_header():
    """Printing the header information"""
    automatron_text_art = pyfiglet.figlet_format("Automatron")
    print(automatron_text_art)
    print("#"*80)
    print(f"Script : {__file__}")
    print("#"*80)
    print("")

#################################################################################

def _init_logger():
    """Initializing the logger"""
    global logger
    logger = logging.getLogger(__name__)
    absolute_log_file_name = "_".join([
        os.path.join(LOGS_DIR,os.path.basename(__file__).split('.')[0]),
        datetime.now().strftime(format="%Y%m%d%H%M%S%f")
    ]) + '.log'

    # Creating handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(absolute_log_file_name)
    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    # Creating formatters
    console_format = logging.Formatter("[ %(asctime)s ] - %(threadName)s - %(levelname)s - %(message)s")
    file_format = logging.Formatter("[ %(asctime)s ] - %(threadName)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_format)
    file_handler.setFormatter(file_format)

    # Adding handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

#################################################################################

def _init_directories():
    """Initializing directories"""
    if not os.path.isdir(LOGS_DIR):
        os.mkdir(LOGS_DIR)
    if not os.path.isdir(INPUT_DIR):
        os.mkdir(INPUT_DIR)
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

#################################################################################

def _create_threads():
    processor_threads = []
    for i in range(PROCESSOR_THREADS):
        processor_threads.append( threading.Thread( target=process, args=() ) )
        processor_threads[i].start()
    return processor_threads

#################################################################################

def _wait_for_threads(processor_threads):
    results = []
    for i in range(PROCESSOR_THREADS):
        results.append(processor_threads[i].join())
    return results

#################################################################################
# Utility Methods ###############################################################
#################################################################################

def print_exec_time(func):
    """Decorator that reports the execution time"""
    def wrap(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        logger.info(f"{func.__name__} completed in [ {str(end_time-start_time)} ]")
        return result
    return wrap

#################################################################################

def print_thread_info(func):
    """Decorator that reports the execution time"""
    def wrap(*args, **kwargs):
        logger.debug(f"Started Thread : PID [ {threading.get_ident()} ] | {threading.current_thread().name}")
        result = func(*args, **kwargs)
        end_time = datetime.now()
        logger.debug(f"Finished Thread : PID [ {threading.get_ident()} ] | {threading.current_thread().name}")
        return result
    return wrap

#################################################################################
# Core Methods ##################################################################
#################################################################################

@print_exec_time
def Initializer():
    """Initializer : To be used for initializing data before processing"""
    pass

@print_thread_info
def process():
    """Processor : To put main processing logic"""
    pass

@print_exec_time
def Executor():
    """Executor : To execute the process in multi-threading mode"""
    processor_threads = _create_threads()
    results = _wait_for_threads(processor_threads)
    logger.info(f"Results from all threads : {results}")

@print_exec_time
def Finalizer():
    """
    Finalizer : 
    To be used for closing database connections, performing clean-ups and post process activities.
    """
    pass

#################################################################################
# M A I N #######################################################################
#################################################################################

if __name__ == "__main__":

    # Pre Steps
    _init_directories()
    _init_logger()
    _print_header()

    # Started batch job
    start_time = datetime.now()

    # Running initializations
    Initializer()

    # Executing core functionality
    Executor()

    # Finalizing
    Finalizer()

    # Finished batch job
    end_time = datetime.now()
    logger.info(f"Batch job finished! Total time taken : [ {str(end_time-start_time)} ]")
