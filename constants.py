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

# The command for opening windows info and id
LIST_APP_COMMAND = 'wmctrl -l'
# The regex used for recognize the id and the name of the apps in the command response of the LIST_APP_COMMAND command
REGEX_LIST_APP_COMMAND = "(0x[0-9a-f]*)[ ]*[0-9\-]*[\s\t]*[^ ]*[ ]*(.*)"