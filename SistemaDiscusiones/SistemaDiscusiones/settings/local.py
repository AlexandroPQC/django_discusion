from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Discusiones',
        'USER': 'alexandro',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS =  [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '15xxxxxxxxxxxxxx'
SOCIAL_AUTH_FACEBOOK_SECRET = 'ffxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

SOCIAL_AUTH_TWITTER_KEY = 'K4xxxxxxxxxxxxxxxxxxxxxx'
SOCIAL_AUTH_TWITTER_SECRET = '7hexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
