"""
Django settings for mysite project.

<<<<<<< HEAD
Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
=======
Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
>>>>>>> d77f5829752f031379513206e62b4778083c0009
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
<<<<<<< HEAD
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tmb)h_10d2a!xe1tap0x-0_4gl(ju)%dv5)lbiy09&o1nf5=_^'
=======
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8ox#s3@0q+5!rkb^_e60r*5q0t$-4q@u4z5$+i6g6exur@p)m6'
>>>>>>> d77f5829752f031379513206e62b4778083c0009

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
<<<<<<< HEAD
=======
    'blog',
>>>>>>> d77f5829752f031379513206e62b4778083c0009
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
<<<<<<< HEAD
        'DIRS': [],
=======
        'DIRS': ['/home/wwc129/PycharmProjects/exchange/mysite/templates'],
>>>>>>> d77f5829752f031379513206e62b4778083c0009
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
<<<<<<< HEAD
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
=======
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'USER': 'wwc129',
        'PASSWORD': 'grewwc080959',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'HOST': 'localhost',
>>>>>>> d77f5829752f031379513206e62b4778083c0009
    }
}


# Password validation
<<<<<<< HEAD
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
=======
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
>>>>>>> d77f5829752f031379513206e62b4778083c0009

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
<<<<<<< HEAD
# https://docs.djangoproject.com/en/1.11/topics/i18n/
=======
# https://docs.djangoproject.com/en/1.10/topics/i18n/
>>>>>>> d77f5829752f031379513206e62b4778083c0009

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
<<<<<<< HEAD
# https://docs.djangoproject.com/en/1.11/howto/static-files/
=======
# https://docs.djangoproject.com/en/1.10/howto/static-files/
>>>>>>> d77f5829752f031379513206e62b4778083c0009

STATIC_URL = '/static/'
