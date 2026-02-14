import re
import os
from os import environ
from Script import script

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Main Variables 

API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
USERNAME = environ.get('USERNAME', "https://telegram.me/Silicon_Official")
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1003519088776'))
MOVIE_GROUP_LINK = environ.get('MOVIE_GROUP_LINK', 'https://infinityaudiosearchinggroup')

# Pics 

QR_CODE = environ.get('QR_CODE', 'https://graph.org/file/ccb9db43e62a2e524928e.jpg')
START_IMG = environ.get('START_IMG', 'https://i.ibb.co/LdT5fdJY/photo-2025-08-13-01-12-38-7537871916074270724.jpg')
FSUB_PICS = (environ.get('FSUB_PICS', 'https://graph.org/file/7478ff3eac37f4329c3d8.jpg https://graph.org/file/56b5deb73f3b132e2bb73.jpg')).split() 

# File Limit

IS_FILE_LIMIT = is_enabled('IS_FILE_LIMIT', True) # Enable Or Disable File Limit
FILES_LIMIT = int(environ.get("FREE_FILES", "3")) #No. of File User Gets In Free

# Database Settings

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://@cluster0.mongodb.net/?retryWrites=true&w=majority")
FILES_DATABASE_URL = environ.get('FILES_DATABASE_URL', "mongodb+srv://@cluster0.mongodb.net/?retryWrites=true&w=majority") # For Files
SECOND_FILES_DATABASE_URL = environ.get('SECOND_FILES_DATABASE_URL', "") # 2nd DB For Files
DATABASE_NAME = environ.get('DATABASE_NAME', "Silicon")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Silicon_Files')

# Verify/Shortlink Settings 

IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1003519088776'))
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1003519088776'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Silicon_Bot_Update")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/Silicon_Bot_Update")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/Silicon_Bot_Update")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "5bb6e402dd86fb8774690a5f4a65d2a2c0c04877")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", 'shortslink.in')
SHORTENER_API2 = environ.get("SHORTENER_API2", "41a89e7a1f16e7dbec0ee52d743f3b5a38a09613")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", 'shortslink2.com')
SHORTENER_API3 = environ.get("SHORTENER_API3", "f287e7e9b1a23c34f542f77787d39607cae36a4d")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", 'shortslink3.online')
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "14400"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "14400"))

# Force Subscribe Settings 

auth_req_channels = environ.get("AUTH_REQ_CHANNELS", "-100")# requst to join Channel for force sub (make sure bot is admin) only for bot ADMINS  
auth_channels = environ.get("AUTH_CHANNELS", "-100")# Channels for force sub (make sure bot is admin)
AUTH_REQ_CHANNELS = [int(ch) for ch in auth_req_channels.split() if ch and id_pattern.match(ch)] 
AUTH_CHANNELS = [int(ch) for ch in auth_channels.split() if ch and id_pattern.match(ch)]

# Channels

SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1003219334269'))
request_channel = environ.get('REQUEST_CHANNEL', '-1003749791880')
REQUEST_CHANNEL = int(request_channel) if request_channel and id_pattern.search(request_channel) else None

# Movie Update Notification Settings/ Auto Index Settings

MOVIE_UPDATE_NOTIFICATION = bool(environ.get('MOVIE_UPDATE_NOTIFICATION', False))  # Notification On (True) / Off (False)
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1003525105249'))  # Notification of sent to your channel
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()] # Auto Index Channel
DELETE_CHANNELS = int(environ.get('DELETE_CHANNELS','-1003781179391')) # Channel to delete file from DB
IMAGE_FETCH = bool(environ.get('IMAGE_FETCH', True))  # On (True) / Off (False)
LINK_PREVIEW = bool(environ.get('LINK_PREVIEW', False)) # Shows link preview in notification msg instead of image
ABOVE_PREVIEW = bool(environ.get('ABOVE_PREVIEW', True)) # Shows link preview above the text in notification msg if True else below the msg
TMDB_API_KEY = environ.get('TMDB_API_KEY', '') # preffer to use your own tmdb API Key get it from https://www.themoviedb.org/settings/api
TMDB_POSTER = bool(environ.get('TMDB_POSTER', False)) # Shows TMDB poster in notification msg
LANDSCAPE_POSTER = bool(environ.get('LANDSCAPE_POSTER', True)) # Shows landscape poster in notification msg

# Bot Settings

AUTO_FILTER = is_enabled('AUTO_FILTER', True)
FILE_AUTO_DEL_TIMER = int(environ.get('FILE_AUTO_DEL_TIMER', '600'))
PORT = os.environ.get('PORT', '5000')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 300))
IMDB = is_enabled('IMDB', True)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', True)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
USE_CAPTION_FILTER = is_enabled('USE_CAPTION_FILTER', False)

# Filters Settings No Need To Change Anything There 

LANGUAGES = [("ʜɪɴᴅɪ", "hin"), ("ᴇɴɢʟɪsʜ", "eng"), ("ᴛᴇʟᴜɢᴜ", "telugu"), ("ᴛᴀᴍɪʟ", "tamil"), ("ᴋᴀɴɴᴀᴅᴀ", "kannada"), ("ᴍᴀʟᴀʏᴀʟᴀᴍ", "malayalam"), ("ʙᴇɴɢᴀʟɪ", "ben"), ("ᴍᴀʀᴀᴛʜɪ", "marathi"), ("ɢᴜᴊᴀʀᴀᴛɪ", "gujarati"), ("ᴘᴜɴᴊᴀʙɪ", "punjabi")]
QUALITIES = [ "240p", "360p", "480p", "540p", "720p", "960p", "1080p", "1440p"]
SEASONS = [("sᴇᴀsᴏɴ 𝟷", "s01"), ("sᴇᴀsᴏɴ 𝟸", "s02"), ("sᴇᴀsᴏɴ 𝟹", "s03"), ("sᴇᴀsᴏɴ 𝟺", "s04"), ("sᴇᴀsᴏɴ 𝟻", "s05"), ("sᴇᴀsᴏɴ 𝟼", "s06"), ("sᴇᴀsᴏɴ 𝟽", "s07"), ("sᴇᴀsᴏɴ 𝟾", "s08"), ("sᴇᴀsᴏɴ 𝟿", "s09"), ("sᴇᴀsᴏɴ 𝟷𝟶", "s10")]

# Stream Settings 

IS_PREMIUM_STREAM = is_enabled('IS_PREMIUM_STREAM', False) # True To Allow Stream For Premium User Only
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1003745029204") # Channel Where Files sent For stream
if len(BIN_CHANNEL) == 0:
    print('Error BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "https://efficient-greer-silicon-develr09-a7dbfae3.koyeb.app/") #App URL Where you deployed
if len(URL) == 0:
    print('error URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('error URL is not valid, exiting now')
        exit()
