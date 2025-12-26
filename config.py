from os import environ

API_ID = int(environ.get("API_ID", "30163640"))
API_HASH = environ.get("API_HASH", "42f349f43dad2c998b0e50b0117c47fd")
BOT_TOKEN = environ.get("BOT_TOKEN", "8546171122:AAFuB-MT27BDRjBDckyCPIZdhAy1Vi80CN4")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003365596711"))
ADMINS = int(environ.get("ADMINS", "5678991839"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
