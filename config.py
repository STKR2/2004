from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "14597561"))
API_HASH = getenv("API_HASH", "8ed6576a27781f3ca14a8fd4c77596d2")
BOT_TOKEN = getenv("BOT_TOKEN", "6399958695:AAGVUEIU277Dbd_SBviW8NJ3B9b73eYzVtc")
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu5ZgOHMNL1UOl6L-9f6Eiu7PPSQij5DjR3dOofA-IG9brvC4JPcBRHsyCphEck3MpDQ8Xor6TJLBCDW4S5Lmp-6YJElNL_KxEFxzNf9wU-U1JP1Hifs9A0Mw01Wos8mUYx-u2Ochogcr81AIpDJTCLPvaKMSpXs-6iaVDfzfj1GtQl-ETjs2_Yv1FF9CAhyyqOagT9k59mJwHEa_NfkouKV0HLlfxapdQOMvqdOA1n9pS19qV075sTH5s4Ki8ZGC9E7n_xNXJDDL2WTltj8E-8y1FXSPghBKOxPYRN7fMWshGPfffHi0cqXpHUog5int77Dr9rhG668ZbF1nQorLpkQ=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "ii4i3")
ALIVE_NAME = getenv("ALIVE_NAME", "music")
BOT_USERNAME = getenv("BOT_USERNAME", "Musiceuro_bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xhsihc")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LKJHG1976")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
