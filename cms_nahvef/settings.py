from pathlib import Path
import os

# Basis
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "change-me-in-production")
DEBUG = False

# Hosts / Proxy / CSRF
ALLOWED_HOSTS = ["beta.nahverkehr-erfurt.de", "127.0.0.1", "localhost"]
CSRF_TRUSTED_ORIGINS = ["https://beta.nahverkehr-erfurt.de"]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "cms_nahvef.urls"

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "cms_nahvef.wsgi.application"

# Datenbank kommt aus separater Datei
from .settings_db import *

# Passwortrichtlinien
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Lokalisierung
LANGUAGE_CODE = "de-de"
TIME_ZONE = "Europe/Berlin"
USE_I18N = True
USE_TZ = True

# Static & Media
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Login-Redirects
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ===== EVB Static/Media (do not remove) =====
from pathlib import Path  # falls oben schon importiert ist, unkritisch
# BASE_DIR ist bereits definiert; falls nicht, dann:
try:
    BASE_DIR
except NameError:
    import os
    BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = "/static/"
STATIC_ROOT = "/var/www/vhosts/nahverkehr-erfurt.de/beta.nahverkehr-erfurt.de/httpdocs/static"

# Pinegrow-Exportquelle im Projekt (hierhin exportierst du CSS/JS/Assets)
STATICFILES_DIRS = [BASE_DIR / "static_src"]

MEDIA_URL = "/media/"
MEDIA_ROOT = "/var/www/vhosts/nahverkehr-erfurt.de/beta.nahverkehr-erfurt.de/httpdocs/media"
# ===== /EVB Static/Media =====
