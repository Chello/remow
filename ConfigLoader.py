import configparser
import cerberus
import constants

class ConfigLoader:
    #Handler for configuration file
    global config_handler

    def __init__(self):
        self.config_handler = configparser.ConfigParser()
        self.config_handler.read("config")
        self.verify_conf_file_connection(self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION])

    def verify_conf_file_connection(self, connection_section):
        config_validator = cerberus.Validator(constants.CONFIG_FILE_SCHEMA_CONNECTION)

        config_validator.empty = False
        # If now is not correct interrupt
        if not config_validator.validate(dict(connection_section)):
            raise Exception(config_validator.errors)


    def connection_type(self):
        return self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION]["ConnectionType"]
