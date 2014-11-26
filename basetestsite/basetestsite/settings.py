import os
from django.utils.translation import ugettext_lazy as _
from dcbase.base_settings import *

DEBUG = True
TEMPLATE_DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'yda$68m_u321d#kh&@zs*0sp(=hbbkm(3(53g@22z*f@m#x(%s'
ROOT_URLCONF = 'basetestsite.urls'
WSGI_APPLICATION = 'basetestsite.wsgi.application'

INSTALLED_APPS = (
    'dcbasetest',
    'allauth.socialaccount.providers.google',
) + INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LANGUAGES = (
  ('de', _('German')),
  ('en', _('English')),
  ('es', _('Spanish')),
  ('fr', _('French')),
  ('it', _('Italian')),
)

