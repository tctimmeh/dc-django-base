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
        'django.contrib.sites',
    
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',
    )
    
    SITE_ID = 1
    
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

### Urls

    url(r'', include('dcbase.urls')),
