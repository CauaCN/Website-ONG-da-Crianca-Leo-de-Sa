"""
Django settings for config project.
...
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

# ----------------------------------------------------------------------
# SEGURANÇA
# ----------------------------------------------------------------------

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG") == "True"

ALLOWED_HOSTS = [
    "ongleodesa.pythonanywhere.com",
    "127.0.0.1"
]

CSRF_TRUSTED_ORIGINS = [
    "https://ongleodesa.pythonanywhere.com",
]

# ----------------------------------------------------------------------
# APLICAÇÕES
# ----------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# ----------------------------------------------------------------------
# TEMPLATES
# ----------------------------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "core" / "templates"
        ],
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

WSGI_APPLICATION = "config.wsgi.application"

# ----------------------------------------------------------------------
# BANCO DE DADOS
# ----------------------------------------------------------------------

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ----------------------------------------------------------------------
# INTERNACIONALIZAÇÃO
# ----------------------------------------------------------------------

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ----------------------------------------------------------------------
# ARQUIVOS ESTÁTICOS
# ----------------------------------------------------------------------

STATIC_URL = "/static/"

# Usa static dentro do core (só se existir)
STATICFILES_DIRS = [
    BASE_DIR / "core" / "static"
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# ----------------------------------------------------------------------
# ARQUIVOS DE MÍDIA
# ----------------------------------------------------------------------

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ----------------------------------------------------------------------
# EMAIL (DESENVOLVIMENTO)
# ----------------------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "no-reply@example.com"
