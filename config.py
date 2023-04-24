from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "13980703"))
API_HASH = getenv("API_HASH", "8739dceb2d5ee894b67b106efc50d52c")
BOT_TOKEN = getenv("BOT_TOKEN", "5649188759:AAFCVbZmDJ7aOqaQzAWTgh3fL8bBYDwnqHc")
SESSION_NAME = getenv("SESSION_NAME", "AgCnmWkNXtrpvXTtn2lNp9A6M88ZQJI3M6hDXoKBC_dt-EwBziBwXYjyLJk-oOhPsggOeUaGazi1yPUdkozD0zVUUvOzUZuJTzdR_Lkg1QWQCLsgJln2urW6Uuz3qGXCy83EPqVvge75Du6KoqrnHh66ULHRd2bHVX5O1P1BstqRNzBeaVxjvHvwbR4CLqNfxL7T3sNoNgCd8O9ns3hzF12mTTZy9TMI_WIs0op2KQ-b_i2csjBWuItp57PL2LrY1zDn1IKsuKBMgWi4jksGTEs8RKFZV48Bik7Wz5geuwu_Sctw1BPPqgQ6G-A98kYs654Et9v966gOImHiQbN4H4YbAAAAAVm0DL4A")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "kurdi_sport")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "meozek2022_bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://t.me/Kalamalnas")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "kurdi_sport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kurdi_sport")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5799939262").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5799939262").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
