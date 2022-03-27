from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'treatment': 0,
    'wait_seconds': 7,
    'doc': "Game untuk Tesis Rizal AS",
}

SESSION_CONFIGS = [
    {
        'name': 'rizal_tesis',
        'display_name': "Rizal Tesis Games",
        'num_demo_participants': 1,
        'app_sequence': ['consent','instruction','game', 'after_survey'],
    },
    {
        'name': 'consent',
        'display_name': 'consent',
        'num_demo_participants':1,
        'app_sequence' : ['consent']
    },
    {
        'name': 'instruction',
        'display_name': 'instruction',
        'num_demo_participants':1,
        'app_sequence' : ['instruction']
    },
    {
        'name': 'game',
        'display_name': 'game',
        'num_demo_participants':1,
        'app_sequence' : ['game']
    },
    {
        'name': 'after_survey',
        'display_name': 'after_survey',
        'num_demo_participants':1,
        'app_sequence' : ['after_survey']
    },
    {
        'name': 'game_after_survey',
        'display_name': 'Game plus After Survey',
        'num_demo_participants':1,
        'app_sequence' : ['game','after_survey']
    }
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# OTREE_PRODUCTION = environ.get('OTREE_PRODUCTION')
# OTREE_AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '09f!o3#&@=4o$@-_vas++o8hv6#9te_c&+cq$w6mp#jl&1qbd('

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
