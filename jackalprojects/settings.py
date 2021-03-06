# -*- coding: utf-8 -*-
"""
Django settings for jackalprojects project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'goak5b2ip1t!gy+bn=ueubq%fh5k$4rr8c!7_=nmlezn81ut@j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'jackal',
    'member',
    'bitcoin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'jackalprojects.urls'

WSGI_APPLICATION = 'jackalprojects.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
   'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': 'jackaldatabase',
          'USER': 'postgres',
          'PASSWORD': 'root',
          'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
FILE_UPLOAD_PERMISSIONS = 0644

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR + '/media'

LOCALE_PATHS = (
     os.path.join(BASE_DIR, 'conf'),
     os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('tr', 'Türkçe'),
    ('en', 'English'),
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'member/templates'),
    os.path.join(BASE_DIR, 'bitcoin/templates'),
    os.path.join(BASE_DIR, 'jackalprojects/templates'),
)

#Admin Log
ADMINS = (
    ('cemkiy', 'se.cemkiy@gmail.com'),
    ('barisariburnu', 'barisariburnu@gmail.com'),
    ('kaykisizcom', 'm.kaykisiz@gmail.com'),)
