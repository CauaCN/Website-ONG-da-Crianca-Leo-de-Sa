"""
Django settings for config project.
...
"""

from pathlib import Path
import os # Importar o módulo os para STATIC_ROOT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "***REMOVED***-w^&6%7o291xz+^2s))qiz*1txh2t=7q($0l-wealg#afe6a*=" # MANTENHA O VALOR COMPLETO ORIGINAL

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # MUDEI PARA FALSE, ESSENCIAL EM PRODUÇÃO

# CORREÇÃO DO DisallowedHost
ALLOWED_HOSTS = ['ongleodesa.pythonanywhere.com', '127.0.0.1'] 


# Application definition

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

# TEMPLATES (Versão Unificada e Correta)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "core" / "templates"],
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


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ... (Omitindo a validação de senha, que está correta) ...


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ----------------------------------------------------------------------
# STATIC FILES (CORREÇÃO DE DEPLOY)
# ----------------------------------------------------------------------

# 1. URL base para servir os arquivos estáticos (CSS/JS)
STATIC_URL = "/static/"

# 2. Diretórios onde o Django procura arquivos estáticos DURANTE O DESENVOLVIMENTO
STATICFILES_DIRS = [
    BASE_DIR / "core" / "static", # Garante que ele busca em core/static
]

# 3. DIRETÓRIO ONDE O 'collectstatic' VAI COPIAR OS ARQUIVOS (NECESSÁRIO PARA PRODUÇÃO)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# Media (uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Outras configurações
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "https://localhost:8000",
    "http://127.0.0.1:8000",
    "https://127.0.0.1:8000",
    "https://ongleodesa.pythonanywhere.com", # Adicionado para produção
]

# Email (Mantido no console para debug)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "no-reply@localhost"
DEFAULT_TO_EMAIL = "cauanovaes15@gmail.com"