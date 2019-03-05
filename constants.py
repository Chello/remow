# That constants are for Cerberus.Validator
# Mandatory sections and dependencies in configuration file
CONFIG_FILE_CONNECTION_SECTION = "Connection"
CONFIG_FILE_SCHEMA_CONNECTION = {
    'connectiontype': {
        'type': 'string',
        'allow_unknown': False,
        'required': True,
        'allowed': ['config', 'prompt', 'command']
    },
    'sshconfigfile': {
        'type': 'string',
        'allow_unknown': False
    },
    'configfilehost': {
        'type': 'string',
        'allow_unknown': False
    },
    'sshcommand': {
        'type': 'string',
        'allow_unknown': False

    }
}
# Name of the VNC Server section
CONFIG_FILE_VNC_SERVER_SECTION = "VNCServer"
CONFIG_FILE_SCHEMA_VNC_SERVER = {
    'startingport': {
        'type': 'integer',
        'allow_unknown': False,
        'required': True,
        'min': 1025,
        'max': 65535
    },
    'secureserver': {
        'type': 'boolean',
        'allow_unknown': False,
        'required': True
    },
    'maxwindows': {
        'type': 'integer',
        'allow_unknown': False,
        'required': True,
        'min': 1
    }
}

# The command for opening windows info and id
LIST_APP_COMMAND = 'wmctrl -l'
# The regex used for recognize the id and the name of the apps in the command response of the LIST_APP_COMMAND command
REGEX_LIST_APP_COMMAND = "(0x[0-9a-f]*)[ ]*[0-9\-]*[\s\t]*[^ ]*[ ]*(.*)"
# The command for create tmp log files
NEWDIR_TMP_LOG = "mkdir -p /tmp/remow"
# Dummy function wich returns the command for create a new server
def NEW_SERVER_ISTANCE(self, appId, serverPort, auth):
    return "x11vnc -id " + appId + " -autoport " + serverPort + " -auth " + auth