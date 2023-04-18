import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "904789"))
    API_HASH = os.environ.get("API_HASH", "2262ef67ced426b9eea57867b11666a1")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6073974860:AAFbAeQ8aDlyZkwRQRzNSrM3kl9TJ5pWBK8")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "622730585")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Surajrathod:Surajrathod.878@cluster0.f8wzeit.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQAmCvXjxtaDNtM5YRBoW53u2RKFas7wGQ03pwIygzuaKTKDEMYkeLYQpOo88Sf1ftxtcA1V7-XQ4RkI6KYEAE7CnC7ZFJuvMnN3fz5dKZT3AF9cThIgO_A57PcDuw54CN7CFguF586pKBYGd4h6m68w16CmA7faF8RmAD9BxOQw-O1Fb83zekJ4NiayOxg_5J-op6NcKLIcwNcRCVcPMEJNZ6izP-FHtR0q2GXVBNH9X8lbmwNtDpJMUnbedPe-bGWO4L8bBgkCaCxbMPUPLdOFW8RW5hu_I7Zxa331E7sHgVlHY_V1wlXKsumTmckt0OZcyyxsyROx5cxV94O__o81O822PAA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001792799649"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "clone_878_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
