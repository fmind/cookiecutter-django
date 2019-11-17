"""Website settings of the project."""

# INITS

SECRET_KEY = ')ske0n&6*ckcm*zn8@pou%$@nca23+iyv3+3mt^ytb2a(l*2!c'

WSGI_APPLICATION = '{{cookiecutter.name}}.wsgi.application'

ROOT_URLCONF = '{{cookiecutter.name}}.urls'

DEBUG = True

# HOSTS

ALLOWED_HOSTS = [
    'localhost',
    '{{cookiecutter.domain}}',
]

# ZONES

LANGUAGE_CODE = '{{cookiecutter.language}}'

TIME_ZONE = '{{cookiecutter.timezone}}'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# STATICS

STATIC_URL = '/static/'

# TEMPLATES

TEMPLATES = [
    {
        'DIRS': [],
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

# APPLICATIONS

INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    '{{cookiecutter.name}}.apps.{{cookiecutter.name|capitalize}}Config',
]

# MIDDLEWARES

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

# DATABASES

DATABASES = {
    'default': {
        'NAME': 'db.sqlite3',
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

# PASSWORDS

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# FRAMEWORKS

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}
