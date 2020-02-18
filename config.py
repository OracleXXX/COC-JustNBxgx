import os

from gmail import gmail

basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    #SECRET KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'

    #RECAPTCHA
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'A-VERY-LONG-SECRET-KEY'
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'A-VERY-LONG-SECRET-KEY'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask Gmail Config
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_POST = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '409602911@qq.com' #os.environ.get('GMAIL_USERNAME') or 'MAIL_USERNAME'
    MAIL_PASSWORD = 'TalentisTF313' #os.environ.get('GMAIL_PASSWORD') or 'MAIL_PASSWORD'