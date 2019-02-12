# That constants are for Cerberus.Validator
# Mandatory sections and dependencies in configuration file
CONFIG_FILE_CONNECTION_SECTION = "Connection"
CONFIG_FILE_SCHEMA_CONNECTION = {
    'connectiontype': {
        'type': 'string',
        'allow_unknown': False,
        'required': True,
        'allowed': ['config', 'prompt']
    },
    'sshconfigfile': {
        'type': 'string',
        'allow_unknown': False
    },
    'configfilehost': {
        'type': 'string',
        'allow_unknown': False
    }
}
