from os import environ

API_ID = int(environ.get("API_ID", "20679071"))
API_HASH = environ.get("API_HASH", "3d088893c7ff5b84c429eadf6df88ab4")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002152956062"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002392980176"))
ADMINS = int(environ.get("ADMINS", "5408428203"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "autoacceptbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
