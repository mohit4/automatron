def assign_logging_from_config( logging_text ):
    """ Method to assign logging level from configurations """
    return {
        "DEBUG" : logging.DEBUG,
        "INFO" : logging.INFO,
        "WARN" : logging.WARN,
        "ERROR" : logging.ERROR,
        "CRITICAL" : logging.CRITICAL
    }.get( 
        logging_text, 
        logging.DEBUG 
    )

def init_configurations():
    """ Method to load configurations from primary config file """

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
    """ Method to generate new log file name with timestamp """
    return "".join( [ 
        JOB_NAME,
        '_',
        datetime.now().strftime('%Y%m%d%H%M%S'),
        '.log'
    ] )

def init_logging():
    """ Method to initialize logging configurations """

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
    global CLI_ARGS
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument( "-c", "--config", help="To provide runtime configuration file" )
    argument_parser.add_argument( "-d", "--create", help="To provide runtime configuration file" )
    CLI_ARGS = argument_parser.parse_args()

def init_directories():
    """ Method to initialize work directories if not exists """
    if not os.path.exists( INPUT_DIR_NAME ):
        os.mkdir( INPUT_DIR_NAME )
    if not os.path.exists( OUTPUT_DIR_NAME ):
        os.mkdir( OUTPUT_DIR_NAME )
    if not os.path.exists( LOG_DIR_NAME ):
        os.mkdir( LOG_DIR_NAME )

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