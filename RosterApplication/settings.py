LOGIN_REDIRECT_URL = 'home'  # Change 'home' to whatever your home page URL name is
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login' 

import os  # Make sure this is at the top

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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