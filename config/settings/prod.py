from .base import *
import os

DEBUG = False

ALLOWED_HOSTS = ["employee-management-system-ee4i.onrender.com"]

SECRET_KEY = os.environ["SECRET_KEY"]


CSRF_TRUSTED_ORIGINS = [
    "https://employee-management-system-ee4i.onrender.com"
]
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
