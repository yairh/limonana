"""
Django settings for limonana project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open("../limonana_conf.json", "r") as f:
    conf = json.load(f)
SECRET_KEY = conf.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "blog",
    "django_summernote",
    "tinymce",
    'grappelli',
    'filebrowser',
    "stdimage",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'limonana.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'limonana.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "limonana",
        "HOST": "localhost",
        "USER": "postgres",
        "PASSWORD": "1234",
        "PORT": "",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'limonana.blog@gmail.com'
EMAIL_HOST_PASSWORD = conf.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

X_FRAME_OPTIONS = 'SAMEORIGIN'
TINYMCE_JS_URL = os.path.join(MEDIA_URL, "js/tinymce/tinymce.min.js")
TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, "js/tinymce")

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,paste,searchreplace,hr,paste,powerpaste,"
               "fullscreen,image imagetools,preview,visualblocks,image,"
               "advlist,table advtable,charmap,lists checklist,emoticons,pageembed",
    'theme': "silver",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'toolbar1':
        '''
                fullscreen preview bold italic underline | fontselect,
                fontsizeselect  | forecolor backcolor | alignleft alignright |
                aligncenter alignjustify | indent outdent | bullist numlist table |
                | link image media | codesample |
                ''',
    'toolbar2':
        '''
                visualblocks visualchars |
                charmap hr pagebreak nonbreaking anchor |  code |
                ''',
    'contextmenu':
        'formats | link image',
    'menubar':
        True,
    'statusbar':
        True,
}
TINYMCE_SPELLCHECKER = True

FILEBROWSER_DIRECTORY = ""

BUENO_ROOT = os.path.join(BASE_DIR, "templates/bueno/")
BUENO_URL = "/bueno/"
