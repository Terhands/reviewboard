# Database backend.  Any supported django database engine should work.
DATABASES = {
    'default': {
        # 'django.db.backends.' followed by one of
        # 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
        'ENGINE': 'django.db.backends.sqlite3',

        # The name of the database. If sqlite3, this should be an absolute
        # path.
        'NAME': '/Users/ter/Documents/School/cmpt405/Project/src/reviewboard/reviewboard.db',

        # Not used with sqlite3
        'USER': '',

        # Not used with sqlite3
        'PASSWORD': '',

        # Set to an empty string for localhost.
        'HOST': '',

        # Set to an empty string for default
        'PORT': '',
    },
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = ")vv)p9c+z9aki8cvz!mx)3&lr9812)18cyc@@$n+chz=nbvt6^"

# Cache backend.  Unset this to turn off caching completely.
#
# In most Installations, memcached is the best option. Development
# installations can get away with a file-based or local memory cache.
#
# CACHE_BACKEND = 'file:///tmp/reviewboard_cache?max_entries=5000'
# CACHE_BACKEND = 'memcached://localhost:11211//'
CACHE_BACKEND = 'locmem:///'

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'US/Pacific'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

# This should match the ID of the Site object in the database.  This is used to
# figure out URLs to stick in e-mails and related pages.
SITE_ID = 1

# Set this to the place of your reviewboard if it does not reside
# at the root of your server. - Add the trailing slash.
# SITE_ROOT = "/reviewboard/"
SITE_ROOT = '/'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# TLS for LDAP.  If you're using LDAP authentication and your LDAP server
# doesn't support ldaps://, you can enable start-TLS with this.
LDAP_TLS = False

# Logging options. DEBUG-level logging is useful for testing.
LOGGING_ENABLED = True
LOGGING_LEVEL = "DEBUG"
LOGGING_DIRECTORY = "."
LOGGING_ALLOW_PROFILING = True

# Enabling DEBUG provides more detailed errors when there are problems,
# and enables use of local media. This should always be enabled for
# development installations.
DEBUG = True

INTERNAL_IPS = "127.0.0.1"


# Selenium testing configuration
#TEST_DATABASE_NAME = "test.db"
#SELENIUM_BROWSER_COMMAND = "*firefox"
#SELENIUM_HOST = "localhost"
#SELENIUM_PORT = 4444
#SELENIUM_LIVE_SERVER_ADDRESS = "127.0.0.1"
