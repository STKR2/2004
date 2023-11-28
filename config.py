from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "27797515"))
API_HASH = getenv("API_HASH", "c425005ffc1d4789025a024cf8416287")
BOT_TOKEN = getenv("BOT_TOKEN", "6394890638:AAHvh2Z7XtAtTMsNvPoQgMuM9BIPtIXkWKY")
SESSION_NAME = getenv("SESSION_NAME", "BAC2TzI1e7RICVUeT0pAQVjDHfNf7ZeahLnBNgMYXQABCXRmaay_kKwgZBIim5rBxOlLnVhriuMpwutDAXXaPKrnlXnW1RN23LfKPSf52GYPPNRYMrh9uQq1z8fF06nirQ-CcnjqDE2uP-I1eXtbmTFLwH5mMguxwOsiJJ4czd4L4LQXbF4fSk39efSxL_is_Kqx3CxM6qOhd78mdIH82kcXdoKWCv1TnmLJb_KenWG20D80i5JWnDJvozXT5Ml0o_-w1aknE9zS8IoCsMt-evhgW6e6lrEc8e8INq_MCGdW1Hzbc2sG-J1GgFeBFsM8C8Jtc22Vcg5BevUuW-BE8qAAAAAX6niAMA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "lPlJI")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "MuiSiCl_BoT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "E_T_L3")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "E_T_L3")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5668167497").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5668167497").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
