from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578"))
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")
BOT_TOKEN = getenv("BOT_TOKEN", "6973158515:AAHiOhCUTQ_zYRIct38SWulsDcCgxzst4Vg")
SESSION_NAME = getenv("SESSION_NAME", "AgAGFRW8AN9biZhAIB_X7rubbTCwNtc48oa-geXlaVsQbV9M1emAEV_iGPw_W-lNP1HGbOuQgF9NAUIxlp8-6rgN16-7Upuhst2wCxewyx0VP7Cxb5k_9EXap6_xeU2v4So9RZMt95XYxhGc4hWO_ikd9P46iHLMjXW8GjQAnGvY-bIrM6XqIXF1yeC3vixEa8knOHGkedZU3FYyLhEILy8TV6eH5jOGvsyw5o7xFElb2zZId_vlYO--B3xSWIMUR6zyH8wozehe9tIn0jZptYjY1rqWOMoYS9wtqvBThVazL60nrgL-KdikJC9beDJLLR0C-wzuAtARPCZ-JK6oG-gVAAAAAUM3evYA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "W7MBoT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "rr8r9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xl444")

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
