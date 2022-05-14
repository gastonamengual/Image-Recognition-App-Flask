from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = True


    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"