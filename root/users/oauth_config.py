import os

from authomatic import Authomatic
from authomatic.providers import oauth2

OAUTH_CONFIG = {
    "Facebook": {  # This name is arbitrary but is easier if it matches the OAuth provider name
        "id": 1,  # These id numbers are arbitrary
        "class_": oauth2.Facebook,  # Use authomatic's Facebook handshake
        "consumer_key": os.getenv("FACEBOOK_ID", "value does not exist"),
        "consumer_secret": os.getenv("FACEBOOK_SECRET", "value does not exist"),
    },
    "Google": {
        "id": 2,  # These id numbers are arbitrary
        "class_": oauth2.Google,
        "consumer_key": os.getenv("GOOGLE_ID", "value does not exist"),
        "consumer_secret": os.getenv("GOOGLE_SECRET", "value does not exist"),
        # Google requires a scope be specified to work properly
        "scope": ["profile", "email"],
    }
}

# Instantiate Authomatic.
authomatic = Authomatic(
    OAUTH_CONFIG,
    os.getenv("AUTHOMATIC_SECRET"),
    report_errors=True,  # Set to False in production
)
