"""
Django settings for webplatform project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from django.core.urlresolvers import reverse_lazy

from unipath import Path

BASE_DIR = Path(__file__).ancestor(3)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ed(t86m^=1eg=ri4m)wrkcq&fhcyttgw8fv&hq=et*ko2%h402'

# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    #'south',
    'rest_framework',
)

LOCAL_APPS = (
    'apps.courses',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'webplatform.urls'

WSGI_APPLICATION = 'webplatform.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-pe'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = [BASE_DIR.child('templates')]

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('home:home')
LOGIN_LOGOUT = reverse_lazy('logout')