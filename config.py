# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "21329703")
    API_HASH = environ.get("API_HASH", "e48ac9efa88bebcf1e3051c4cc39d35b")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7138807184:AAF2eVZn1kfFX9SPWQqxeb0vIOY4z8LBMYU") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6738911549').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://autofilterbot1:autofilterbot1@autofilterbot1.d8wmo.mongodb.net/?retryWrites=true&w=majority&appName=autofilterbot1")
    DATABASE_NAME = environ.get("DATABASE_NAME", "autofilterbot1")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002171340177'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/+kgi3W0EEvG03ZGU9") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
