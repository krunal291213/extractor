import os

API_ID = 25134698

API_HASH = os.environ.get("API_HASH", "6b66c879f765a0662a3ad030f8ae45f7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8401746480:AAHBirdzBtMHPM6Y9RhuY1yzzFOMs1EFKYU")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "7425217769"))

LOG = int(os.environ.get("LOG", "1"))

PORT = os.environ.get("PORT", "8080")

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7376514183").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
