from os import environ, path
from dotenv import load_dotenv

load_dotenv(path.join(path.abspath('.'), '.env'))

class Config():
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')

    #Mail
    MAIL_SERVER = environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = environ.get('MAIL_PORT') or 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    ADMINS = ['sowgatfilm@gmail.com', 'muhammedjepbarov@gmail.com']
    
   

    #Database
    SQLALCHEMY_ECHO = 0
    SQLALCHEMY_DATABASE_URI = 'sqlite:///doly.db'

    