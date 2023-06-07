import environ
import json
import os

from django.core.exceptions import ImproperlyConfigured

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('fairPay')
MEDIA_DIR = ROOT_DIR.path('fairPay/media')
SERVER_STATIC_DIR = environ.Path(__file__) - 4

with open(ROOT_DIR("secrets.json")) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Definir la variable de ambiente {0}".format(setting)
        raise ImproperlyConfigured(error_msg)

ALLOWED_HOSTS = get_secret("ALLOWED_HOSTS")
INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']

LANGUAGE_CODE = 'es'
SITE_ID = 1
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_L10N = True

DEBUG = get_secret('DEBUG')
DATABASE_DEFAULT = get_secret('DATABASE_DEFAULT')
SECRET_KEY = get_secret('SECRET_KEY')

# ---- CONFIG TAMAÑO MÁXIMO DE ARCHIVOS SUBIDOS
DATA_UPLOAD_MAX_MEMORY_SIZE = 100*1024*1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 100*1024*1024

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

DATABASES = {
    'default': DATABASE_DEFAULT,
}

# APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'fairPay.orders'
]

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    #'allauth.account.auth_backends.AuthenticationBackend',
]

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'django_currentuser.middleware.ThreadLocalUserMiddleware',
]

# STATIC
STATIC_ROOT = str(SERVER_STATIC_DIR('static_collected'))
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    str(APPS_DIR.path('static')),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = str(MEDIA_DIR)
TEMPLATE_URL = '/templates/'
# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(APPS_DIR), "fairPay", "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ADMIN
ADMIN_URL = r'^admin/'
ADMINS = [
    ("admin", 'dianagarco@gmail.com'),
]
MANAGERS = ADMINS