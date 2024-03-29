#!/usr/bin/env/python

""" 

automatron.py :

Automatron is a Python Batch Script automatic code generation tool.

"""

__author__ = "Mohit Kumar"
__credits__ = ["Mohit Kumar"]
__version__ = "1.0.0"
__maintainer__ = "Mohit Kumar"
__email__ = "mohitkumar2801@gmail.com"
__status__ = "Production"

import os
import sys
import argparse
import yaml

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument( '-c', '--create', help='Name of the job.' )
args = argument_parser.parse_args()

CONFIG_FILE_NAME = 'config.yaml'

SNIPPETS_DIR = "snippets"
BASE_DIR = "base"
SNIPPET_FILE_NAMES = (
    "imports.py",
    "globals.py",
    "methods.py",
)
SNIPPETS_PATH = None

BASIC_CONFIG = {
    "logging": "DEBUG"
}

HEADER_SNIPPET = """#!/usr/bin/env/python

\"\"\" %s : This script is generated by Automatron \"\"\"

__author__ = "John Doe"
__credits__ = ["John Doe"]
__version__ = "1.0.0"
__maintainer__ = "John Doe"
__email__ = "JohnDoe@gmail.com"
__status__ = "Prototype"

"""

TAILER_SNIPPET = """
if __name__ == "__main__":

    initialize()
    execute()
    finalize()
"""


def fetch_env_path():
    """ Method to fetch and populate the global value in SNIPPETS_PATH """
    global SNIPPETS_PATH
    path_data = os.environ['PATH']
    SNIPPETS_PATH = [ x for x in path_data.split(';') if 'automatron' in x ][0]

def create_config_file():
    """ Method to create a configuration file """
    with open( os.path.join( JOB_NAME, CONFIG_FILE_NAME ), 'w' ) as config_file:
        data = yaml.dump( BASIC_CONFIG, config_file )
    print( f"Created the configuration file : { JOB_NAME }/{ CONFIG_FILE_NAME }" )

def create_basic_file():
    """ Method to create a basic python batch script """
    with open( os.path.join( JOB_NAME, JOB_NAME+'.py' ), "w" ) as mainScript:
        mainScript.write( HEADER_SNIPPET%( args.create ) )

        for SNIPPET_FILE in SNIPPET_FILE_NAMES:
            with open( os.path.join( SNIPPETS_PATH, SNIPPETS_DIR, BASE_DIR, SNIPPET_FILE ) ) as snippet_file:
                mainScript.write( "".join( snippet_file.readlines() ) )
                mainScript.write( "\n\n" )
        
        mainScript.write( TAILER_SNIPPET )
    print( f"Created Job Script : { JOB_NAME }/{ JOB_NAME }.py" )


if __name__ == "__main__":
    
    global JOB_NAME

    if args.create:

        JOB_NAME = args.create

        print( f"Starting project generation for Job Name : { JOB_NAME }" )

        if not os.path.exists( JOB_NAME ):
            os.mkdir( JOB_NAME )

        fetch_env_path()
        create_config_file()
        create_basic_file()

    else:
        print( f"No job name provided, exiting!" )
        sys.exit( os.EX_NOINPUT )