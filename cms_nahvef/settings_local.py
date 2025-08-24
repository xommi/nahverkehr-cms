from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ["beta.nahverkehr-erfurt.de", "127.0.0.1", "localhost"]

TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [ BASE_DIR / "templates" ],
    "APP_DIRS": True,   # nutzt filesystem + app_directories automatisch
    "OPTIONS": {
        "context_processors": [
            "django.template.context_processors.debug",
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
        ],
    },
}]
# ---- static files (added) ----
STATIC_URL = '/static/'
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = BASE_DIR / 'static'   # Zielordner für collectstatic
# ==== static / WhiteNoise (added) ====
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Gzip + Manifest (Cache-Busting)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# WhiteNoise direkt nach SecurityMiddleware einschleusen
try:
    i = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
    if 'whitenoise.middleware.WhiteNoiseMiddleware' not in MIDDLEWARE:
        MIDDLEWARE.insert(i+1, 'whitenoise.middleware.WhiteNoiseMiddleware')
except Exception:
    # Falls MIDDLEWARE noch nicht existiert (unwahrscheinlich, aber sicher ist sicher)
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ] + list(globals().get('MIDDLEWARE', []))
# ==== Reverse-Proxy / Admin / Middleware (added) ====
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
CSRF_TRUSTED_ORIGINS = ['https://beta.nahverkehr-erfurt.de']

_required = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

try:
    MIDDLEWARE  # existiert evtl. schon in den Basiseinstellungen
except NameError:
    MIDDLEWARE = []
# erforderliche Einträge vorn sicherstellen, Rest hinten anhängen
_rest = [m for m in MIDDLEWARE if m not in _required]
MIDDLEWARE = _required + _rest

# WhiteNoise entfernen (statische Dateien liefert Apache aus)
MIDDLEWARE = [m for m in MIDDLEWARE if m != 'whitenoise.middleware.WhiteNoiseMiddleware']

# Admin/Grundlagen sicherstellen
try:
    INSTALLED_APPS
except NameError:
    INSTALLED_APPS = []
for app in [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]:
    if app not in INSTALLED_APPS:
        INSTALLED_APPS.append(app)
# ==== Produktion / Sicherheit ====
DEBUG = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE    = True
SECURE_SSL_REDIRECT   = True

# HSTS: erst aktivieren, wenn HTTPS sicher überall funktioniert.
# Für den Start klein (5 Min), später z.B. 1 Jahr.
SECURE_HSTS_SECONDS = 300
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = False  # erst auf True, wenn du preload wirklich willst
