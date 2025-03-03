import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "500"))

DEVS = list(map(int, os.getenv("DEVS", "1344553362").split()))

API_ID = int(os.getenv("API_ID", "25914558"))

API_HASH = os.getenv("API_HASH", "c3ca9605a1556a4e55d84dc4e7f80346")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7110295005:AAGtrVJIbve4fm2rm2GvY-Ijmtvsx5IkCMw")

OWNER_ID = int(os.getenv("OWNER_ID", "6039924260"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ryuxakun:Mantap1245@cluster0.1j1cw.mongodb.net/ryuxakun?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002216932703"))