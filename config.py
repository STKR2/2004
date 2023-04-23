from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578"))
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")
BOT_TOKEN = getenv("BOT_TOKEN", "5204315005:AAEAISUpvY9N4UV-YB150KWlOUcM-0eejj0")
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuxafyrFFoC-LRy3CmqexdbIUSCkmMnuAaJ5FfgqcR3oTTu1FDeQZeviEx6zAZJR3kHEwiJdhrYnaWnxLPXOUBLpdCVnb1g59QzM5Vjpa813TZSRAzXA_VW2QiUPix6Llb0vINyqTt5Gla9GHA60OX_UjjWr4nG4d6NX6V7S58bvF1XDbrOUJhho2eeleVg0lwlWbWY7zqOhjH3xST20ryphfmIophRgg02f1bh9rUGH3OAjfB9ZDW1UPPk8rDzJnjs9yHNt6Mr2mqUa4FcYqUk0dXyAgvhVuM7jX-U89NXlU_0wgKAXzvnvse-NUx3zDwPOKL9zbHuE90LIF3kAmdSg=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "rr8r9")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Saiadjabot")
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
