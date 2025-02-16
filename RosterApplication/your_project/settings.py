# Update ALLOWED_HOSTS to include your pythonanywhere domain
ALLOWED_HOSTS = ['clarkdjcr.pythonanywhere.com', 'localhost', '127.0.0.1']

# Set DEBUG to False for production
DEBUG = False

# Configure static files
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# If you're using media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/' 