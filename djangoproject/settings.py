"""
Django settings for djangoproject project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k$e=di3m)+&yzm#55xbtpyv4#ex_v-(lhz74g^@6xv6cb4gb&w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['django.local', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'adminsector.apps.AdminsectorConfig',
    'adminlte3',
    'adminlte3_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'widget_tweaks',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps
    'crispy_forms',
    'crispy_bootstrap4',

    'pymage.apps.PymageConfig',
    'accounts.apps.AccountsConfig',
]


AUTH_USER_MODEL = 'accounts.CustomUser'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoproject.urls'
TEMPLATES_DIR_PYIMG = os.path.join(BASE_DIR, 'pymage/templates')
TEMPLATES_DIR_ACC = os.path.join(BASE_DIR, 'accounts/accounts_templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR_PYIMG, TEMPLATES_DIR_ACC,],
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

WSGI_APPLICATION = 'djangoproject.wsgi.application'
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kathmandu'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
from pathlib import Path
BASE_DIR_PATH = Path(__file__).resolve().parent.parent
# STATIC_ROOT = Path.joinpath(BASE_DIR_PATH, "static/")
STATIC_URL = '/static/'
STATICFILES_DIRS = (Path.joinpath(BASE_DIR_PATH, 'static/'),)
MEDIA_ROOT = os.path.join(BASE_DIR, "media/user_profiles")
MEDIA_URL = '/media/'

EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tempmailtest57@gmail.com' #your email-id
EMAIL_HOST_PASSWORD = 'xxou krce lzuu hofp' #your password
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

print('Base Directory = =>',BASE_DIR)
print('Media Directory = =>',MEDIA_ROOT)
print('Medai Url Directory = =>',MEDIA_URL)
print('Static  Directory = =>',STATICFILES_DIRS)
