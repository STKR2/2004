from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "25449636"))
API_HASH = getenv("API_HASH", "b502058c5b53c90017d363b69f87e492")
BOT_TOKEN = getenv("BOT_TOKEN", "5385370603:AAHjSbZFL1OLl_uOm3v8lS0iKSYhRJS_bKs")
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu13zqqicqI6mGRTxKp7KowN-2B8TrYYEOCCXbb2rFWI8GcLVkcV3ylzkbQv-e_1YjABlKA5m5C7BY27l1SPGA0XRFoEKkWQAJvV_X4dZDFhQCgF1C2ljktl8bmmXHwmZ327nsl54Pyv13cfPRr8EPGzKz65rX0q249FivLw2YvhuMHtMR0T0dPe2IvXg6dhQ4YA0z5GDvkGBMrjhFNDjK9c7_ehPeZDIe0iBg4xkc5Sa9W0rbvrRGKHgpu88bD-EhA5fYnHnRgVj91917LCVDHlg1K8wNwGZJ6Q2ZwDkjhrz3sLD4WVNZTC4rzf-7gW992ud1zOUHU55y1AXbHBOtFA=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "L1_X5")
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
