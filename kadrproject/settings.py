"""
Django settings for kadrproject (Жұман Аян фотостудиясы — landing).
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Тек жергілікті/оқу мақсатына арналған кілт. Продакшенге шығарар алдында ауыстырыңыз.
SECRET_KEY = 'django-insecure-kadr-project-local-dev-key'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'landing',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'kadrproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'kadrproject.wsgi.application'

LANGUAGE_CODE = 'kk'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
