from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd4fbmjdv45huco',
        'USER': 'sxuwzgqzklnact',
        'PASSWORD': 'xfkWkyYN02R-ByMgMvNEAWP-w5',
        'HOST': 'ec2-54-225-101-64.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR.child('static')]

STATIC_ROOT = 'staticfiles'