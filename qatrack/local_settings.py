# Set to True to enable debug mode (not safe for regular use!)
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'qatrackplus31',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'CAP02014E1CS\SQLEXPRESS',  # leave blank unless using remote server or SQLExpress (use 127.0.0.1\\SQLExpress or COMPUTERNAME\\SQLExpress)
        'PORT': '',  # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
    # 'readonly': {
    #     'ENGINE': 'sql_server.pyodbc',
    #     'NAME': 'qatrackplus31',
    #     'USER': 'qatrack_reports',
    #     'PASSWORD': 'qatrack_reports',
    #     'HOST': 'CAP02014E1CS\SQLEXPRESS',  # leave blank unless using remote server or SQLExpress (use 127.0.0.1\\SQLExpress or COMPUTERNAME\\SQLExpress)
    #     'PORT': '',  # Set to empty string for default. Not used with sqlite3.
    #     'OPTIONS': {
    #         'driver': 'ODBC Driver 17 for SQL Server'
    #     },
    # }
}

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', "*"]

# needs to be set to True when running behind reverse proxy (normal deploy)
# set to False when not running behind reverse proxy
# Use True for e.g. CherryPy/IIS and False for Apache/mod_wsgi
USE_X_FORWARDED_HOST = True

# If you host your QATrack+ instance at a non root url (e.g. 12.345.678.9/qatrack)
# then you need to uncomment (and possibly modify) the following settings
# FORCE_SCRIPT_NAME = "/qatrack"
# LOGIN_EXEMPT_URLS = [r"^qatrack/accounts/", r"qatrack/api/*"]
# LOGIN_REDIRECT_URL = '/qatrack/qa/unit/'
# LOGIN_URL = "/qatrack/accounts/login/"


# Who to email when server errors occur
ADMINS = (
    ('sa', 'josel.leon.garcia.sspa@juntadeandalucia.es'),
)
MANAGERS = ADMINS

# Email and notification settings
# EMAIL_NOTIFICATION_USER = None
# EMAIL_NOTIFICATION_PWD = None
# EMAIL_NOTIFICATION_TEMPLATE = "notification_email.html"
# EMAIL_NOTIFICATION_SENDER = "qatrack@yourmailhost.com"
# use either a static subject or a customizable template
# EMAIL_NOTIFICATION_SUBJECT = "QATrack+ Test Status Notification"
# EMAIL_NOTIFICATION_SUBJECT_TEMPLATE = "notification_email_subject.txt"

EMAIL_FAIL_SILENTLY = True
EMAIL_HOST = ""  # e.g. 'smtp.gmail.com'
EMAIL_HOST_USER = ''  # e.g. "randle.taylor@gmail.com"
EMAIL_HOST_PASSWORD = 'your_password_here'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Madrid'


# By default, cache is stored at qatrack/cache/cache_data/, but can be set at any location, as well as the timeout:
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': 'C:/deploy/qatrackplus/qatrack/cache/cache_data',
        'TIMEOUT': 72*60*60, # cache timeout of 72hours, for disk memory economy
    }
}


# Precision to use when displaying constant values
CONSTANT_PRECISION = 8


# By default QATrack+ will show icons to indicate the pass/fail or due/overdue/not due status of tests and test lists
ICON_SETTINGS = {
    'SHOW_STATUS_ICONS_PERFORM':  True,
    'SHOW_STATUS_ICONS_LISTING':  True,
    'SHOW_STATUS_ICONS_REVIEW':  True,
    'SHOW_STATUS_ICONS_HISTORY':  False,
    'SHOW_REVIEW_ICONS':  True,
    'SHOW_DUE_ICONS':  True,
    'SHOW_STATUS_LABELS_LISTING': True,
    'SHOW_REVIEW_LABELS_LISTING': True,
    'SHOW_STATUS_LABELS_REVIEW': True
}


# This is the warning message given to the user when a test result is out of tolerance
# Override this setting in local_settings.py to a locally relevant warning message
DEFAULT_WARNING_MESSAGE = "NO APTO"

# Display ordering on the "Choose Unit" page. (Use "name" or "number")
ORDER_UNITS_BY = "number"

# Enable or disable the "Difference" column when reviewing test lists
REVIEW_DIFF_COL = True

# default display settings for test statuses
TEST_STATUS_DISPLAY = {
    'fail': "Fail",
    'not_done': "Not Done",
    'done': "Done",
    'ok': "OK",
    'tolerance': "Tolerance",
    'action': "Action",
    'no_tol': "No Tol Set",
}

# default short display settings for test statuses
TEST_STATUS_DISPLAY_SHORT = {
    'fail': "Fail",
    'not_done': "Not Done",
    'done': "Done",
    'ok': "OK",
    'tolerance': "TOL",
    'action': "ACT",
    'no_tol': "NO TOL",
}


# To let users restore or change their password by themselves, set to True (default):
ACCOUNTS_PASSWORD_RESET = True

# To let anonymous users register themselves, set to True; however it's better set it to False (default) to control the staff
ACCOUNTS_SELF_REGISTER = False

# Not to care cases; let set it False (default) so caps matter
ACCOUNTS_CLEAN_USERNAME = False

# Chrome path for generating PDF reports
CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

# To show category in each test (False) or just in the first test (True) sharing the same category:
CATEGORY_FIRST_OF_GROUP_ONLY = True

# To use Black for autoformatting:
COMPOSITE_AUTO_FORMAT = True

# Set number formatting: keys = New, no keys = Old, f = decimal positions, e = scientific format, g = general format
DEFAULT_NUMBER_FORMAT = "{:.3f}"  # 3 decimal place fixed precision using "New" style formatting

# Set the maximum number of tests per test list (200 by default)
MAX_TESTS_PER_TESTLIST = 200

# Adjust the number of historical test results to show when reviewing/performing QC (5 by default)
NHIST = 5

# Control how often (in seconds) the server is pinged when performing QC or entering service log data;
# set to 0 to disable ping check (5 by default)
PING_INTERVAL_S = 5

# To allow users to update the review and approval status of multiple test list instances at the same time (False by default)
REVIEW_BULK = True

# Create service event without giving any information
SL_ALLOW_BLANK_SERVICE_AREA = True
SL_ALLOW_BLANK_SERVICE_TYPE = True

# Let users to be logged in indefinitely; otherwise SESSION_COOKIE_AGE = d x 24 x 60 x 60 (by default 14 days)
SESSION_SAVE_EVERY_REQUEST = True