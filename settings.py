from logic import SchemaManager as sm

sm.loadAllSchemas()

DOMAIN = sm.getDomainSetting()

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'bg'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

URL_PREFIX = "api"

ENFORCE_IF_MATCH = False

SEND_FILE_MAX_AGE_DEFAULT = 0

PAGINATION = False

DEBUG = False
TESTING = False

SERVER_NAME = '35.188.166.90:80'

X_DOMAINS = '*'
X_HEADERS = ['Authorization','Content-type']

CACHE_CONTROL = 'no-cache, no-store, must-revalidate'