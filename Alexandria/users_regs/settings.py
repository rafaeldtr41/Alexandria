# EmailProject/settings.py
# This should be at the start of the file
import environ

env = environ.Env()
environ.Env.read_env()

# Previous settings ...
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
