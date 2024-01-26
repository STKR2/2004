from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID")27188054)
API_HASH = getenv("API_HASH"03cf971d70a86171fffa0eb22227849c)
BOT_TOKEN = getenv("BOT_TOKEN"@IIIOLWBOT)
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu4zJEfTllOkPMDWwWorlYBxtTtp-tS4NYWV0hB7qo3gntq7u9_GtoTc-ppRHwFuiZhb6w3qvWs2QbuX_Tm1_uXWpuFxfMV6QHgAjRsXWo0t0Lj0hcc0snSGVpB8unXLsp6iGQf1EioFxPzC4aQ2Ex9laKTWscXtE5RfmygwTTNgcxIl7804K8uSE7Dts8_pbwWBVF8ZNsMpJn25CpjocaWgvi5F-kjuYfo_EgyPXP9Ck24cTYFEqm0md8yeBFdv-qZbmp4RhQvmrfAaicRouJLIsiXuZHh8H5pRV1_-1CpM2CXJTK8YDH8cjs2Lf-YqDD5wwfj-e7O92cIy3gdzj3ts=")

# mandatory vars
OWNER_USERNAME = getenv("@Xs_UB")
ALIVE_NAME = getenv("AHMAD")
BOT_USERNAME = getenv("جيمثون")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/63300139d232dc12452ab.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")

# language
LANGUAGE = getenv("BOT_LANGUAGE", "en")
