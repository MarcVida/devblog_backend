from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'marcvida$test_db',
        'HOST': 'marcvida.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'USER': 'marcvida',
        'PASSWORD': 'pass12345',
    }
}