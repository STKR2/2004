from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "20272463"))
API_HASH = getenv("API_HASH", "4044459cd2988126c15d628b1d67a25a")
BOT_TOKEN = getenv("BOT_TOKEN", "5557419876:AAH1qlp8lpwj7m4heK9cFDDlHBPX-FySgH0")
SESSION_NAME = getenv("SESSION_NAME", "BAE1VU8AtXdXz6_OtRqm0z9Pt5LOpKEl7FQHRc-ziRzc8LDTvBsYpIJtu24osy2nh6lqaeOKUTvjOa_VmdjSpIjqQ-k6v82RSo3RZFTpCv0axfHA5DF2bdb-afo6kxQDKNhUt-6CKZWgnfIXmqEe5h-0dYycIrEowoeYbXlk7RST_er6eKVB4L19Fjt75GYVLodIkMeVie-OvPnU3efJn5bVtP9PPAtKhigvfueKA3wznf1FvvTjkHVjUlcmMKd5j5eLTy2AwUCXFYI4uyPzV7j3ZvMCLB-AU2ia1zAzNOQOdhiATFKf64vCmYHWqd7bEOMU7ONy3xBST9iXhaHMEasMuxdmzQAAAAFb61QJAA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "BotDarbakaabnbott")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "BotDarbakaabnbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VV_OG")
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
