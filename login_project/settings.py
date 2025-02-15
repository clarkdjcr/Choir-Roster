import os

# Get the base directory of your project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'user_list'
LOGOUT_REDIRECT_URL = 'login'

# Set DEBUG to True for development
DEBUG = True

# Add localhost to ALLOWED_HOSTS
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/Volumes/SSD/Choir Projects/Choir-Roster/RosterApplication/templates',  # Update to include Choir-Roster
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

# Make sure there's no extra indentation here
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    '/Volumes/SSD/Choir Projects/Choir-Roster/RosterApplication/static',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ROOT_URLCONF = 'login_project.urls'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h9d7f0q^dz7t4@!p3$w2y#n8m5k2l6j9'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = '/Volumes/SSD/Choir Projects/Choir-Roster/RosterApplication/media'

# Make sure the media directory exists
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

# Add or update these email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'clarkdjcr@gmail.com'  # Replace with your Gmail address
EMAIL_HOST_PASSWORD = 'usvc kpjm mwhx mscp'  # Replace with your Gmail App Password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# For development/testing, you can use this instead to see emails in the console:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Add CSRF settings
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8003']  # Add your development server 