"""
Django settings for PicProcure project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eltc&$to4ee@=nmz(rv(l%ijo0zd+r-bpsrl(i&1h-+@xls@w$'

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
    'uploadFiles.apps.UploadfilesConfig',
    'users.apps.UsersConfig',
    'events.apps.EventsConfig',
    'storages',
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

ROOT_URLCONF = 'PicProcure.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'PicProcure.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'PicProcure',
        'USER':'root',
        'PASSWORD':'',
        'HOST': 'localhost',
        'PORT':'3306',
    }
}
<<<<<<< HEAD

=======
>>>>>>> faf04c06a4dcdb0fe212c22db06ab380c9c4556f
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'picprocure@gmail.com'
EMAIL_HOST_PASSWORD = 'ashsamriya'
EMAIL_PORT = 25
<<<<<<< HEAD
=======

>>>>>>> faf04c06a4dcdb0fe212c22db06ab380c9c4556f
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
#MEDIA_URL = '/media/'
#STATIC_URL = '/static/'
# this is the static files folder name which you created in django project root folder. This is different from above STATIC_URL. 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'statics'),
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
#STATICFILES_STORAGE = 'PicProcure.custom_azure.AzureMediaStorage'
#STATIC_LOCATION = "static"


AZURE_ACCOUNT_NAME = "picprocurestorageaccount"
AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
MEDIA_LOCATION = "media"
STATIC_URL = '/static/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/'

MEDIA_ROOT='http://{AZURE_ACCOUNT_NAME}.blob.core.windows.net'