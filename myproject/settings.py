import os


INSTALLED_APPS = [...'myapp'];

STATIC_URL = '/static/';
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles');

DEBUG = False
ALLOWED_HOSTS = ['.elasticbeanstalk.com']
