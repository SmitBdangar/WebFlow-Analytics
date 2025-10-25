"""
Django settings for webflow project.
"""

from pathlib import Path
import os
# Importing os again here for convenience with static files, 
# although it was imported later in your original file.


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Use pathlib for BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-g47^iqw@v1cq8u-(*0663je7skz=(cbzf-z)r)%0$rby-e#^y^'

# ⚠️ DEBUG MUST BE TRUE FOR LOCAL DEVELOPMENT, FALSE FOR PRODUCTION
DEBUG = False # Set to True when developing locally!

ALLOWED_HOSTS = ['webflow-analytics-production.up.railway.app', '127.0.0.1', 'localhost']


CSRF_TRUSTED_ORIGINS = [
    'https://webflow-analytics-production.up.railway.app',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tracker',
]

MIDDLEWARE = [
    # 🌟 NEW: WhiteNoise must be first after SecurityMiddleware
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware", 
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware", # Added for completeness
]

ROOT_URLCONF = 'webflow.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
        ]},
    },
]

WSGI_APPLICATION = 'webflow.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# ----------------------------------------------------
# 🌟 STATIC FILES CONFIGURATION (CRITICAL FOR RAILWAY)
# ----------------------------------------------------

# 1. The base URL for static files (remains 'static/')
STATIC_URL = 'static/'

# 2. Where Django should look for static files during development and collectstatic
# This points to your top-level 'static' directory.
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# 3. Where 'collectstatic' will dump all files for deployment
# WhiteNoise will serve files from this directory.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 4. WhiteNoise storage backend for compression and caching
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = 'login'


# ----------------------------------------------------
# MAXMIND CONFIGURATION (As in your original file)
# ----------------------------------------------------
# Re-define BASE_DIR using os.path for MAXMIND_DB_PATH compatibility if needed, 
# though using the pathlib BASE_DIR is cleaner.
# Assuming tracker is an app inside BASE_DIR
MAXMIND_DB_PATH = BASE_DIR / "tracker" / "geo" / "GeoLite2-City.mmdb"