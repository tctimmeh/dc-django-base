# DC Django Base

## Installation

### Settings

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.request",
        "allauth.account.context_processors.account",
        "allauth.socialaccount.context_processors.socialaccount",
    )
     
    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )
    
    INSTALLED_APPS = (
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',
        'widget_tweaks',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.sites',
    )
    
    SITE_ID = 1
    
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

For e-mail verification on user accounts be sure to enable it in settings:

    ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

For development set a console email backend instead:

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 

### Urls

    url(r'', include('dcbase.urls')),
