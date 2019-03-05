import configparser
import cerberus
import constants
from sshconf import read_ssh_config, empty_ssh_config
from os.path import expanduser

class ConfigLoader:
    #Handler for configuration file
    global config_handler

    def __init__(self):
        self.config_handler = configparser.ConfigParser()
        self.config_handler.read("config")
        self.validate_conf_file_connection(self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION])


    def validate_conf_file_connection(self, connection_section):
        self.verify_conf_file_connection(connection_section)
        # Checking dependencies
        if self.connection_type() == "config":
            constants.CONFIG_FILE_SCHEMA_CONNECTION['sshconfigfile']['required'] = True
            constants.CONFIG_FILE_SCHEMA_CONNECTION['configfilehost']['required'] = True
            self.verify_conf_file_connection(connection_section)
        
        elif self.connection_type() == "command":
            constants.CONFIG_FILE_SCHEMA_CONNECTION['sshcommand']['required'] = True
            self.verify_conf_file_connection(connection_section)

    def verify_conf_file_connection(self, connection_section):
        config_validator = cerberus.Validator(constants.CONFIG_FILE_SCHEMA_CONNECTION)

        config_validator.empty = False
        # If now is not correct interrupt
        if not config_validator.validate(dict(connection_section)):
            raise Exception(config_validator.errors)

    def get_conf_connection_attribute(self, attribute):
        """Return the value specified in the attribute for the connection section"""
        if attribute in self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION]:
            return self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION][attribute]
        else:
            return None

    def connection_type(self):
        """Returns the connection type in ConfigFile"""
        return self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION]["ConnectionType"]
    
    def ssh_config_file(self):
        """Returns the configuration for connecting to the ssh server"""
        if (
            "ConnectionType" in self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION]
            and "config" == self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION]["ConnectionType"]
            and "SSHConfigFile" in self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION]
            and "ConfigFileHost" in self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION]
            ):
            c = read_ssh_config(expanduser("~/.ssh/config"))

            return c.host(self.config_handler[constants.CONFIG_FILE_CONNECTION_SECTION]["ConfigFileHost"])  # print the settings
        else:
            return None

    def get_conf_vncserver_attribute(self, attribute):
        """Return the value specified in the attribute for the VNCServer """
        if attribute in self.config_handler[constants.CONFIG_FILE_VNC_SERVER_SECTION]:
            return self.config_handler[constants.CONFIG_FILE_VNC_SERVER_SECTION][attribute]
        else:
            return None

    def get_conf_section_attribute(self, section, attribute):
        """ Returns the given attribute of a given section.
            Returns an Exception if the specified section or attribute does not exists."""
        if (
            section in self.config_handler and
            attribute in self.config_handler[section]
            ):
            return self.config_handler[section][attribute]
        else:
            raise Exception
