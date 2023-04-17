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
    SESSION = os.environ.get("SESSION", "BQANzlUAqZOAf3bccmYIU-QFbQbp7Z_hvvtWH6NLminUXm7eYyPs2caNZMe-qLZR88ZBRPapctq6PBI3JgTRZcBjhi4mmu_o6kiw6N83plLNeFp56Yuuxg_WVMBQZuzFNqu9-WkWj2-Jp0DMibWvD2qnozpDj5XigygYAIr-zj6JcLG07fifsxTVoJ9Vybvup5Sy-qQCVupbiMQOMNud3UzYkYc0hvYhPaKNjknEYjAroYzDGk3BROLq2wFKeh0RfyxbdeHGRu29ed82F0PRiM5N3Dl7JEkb5ZImOXhhLW-dU8ynALetJUjgB1Wh4z3UKVRLpwKWWgeUTYdhGNQxLkVGkL3iNgAAAAA7zbY8AA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001792799649"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@clone_878_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
